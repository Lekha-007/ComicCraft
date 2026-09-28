import json
import re
import time

from google import genai
from app.config import settings


def extract_json(text: str):
    text = text.strip()

    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text)
        text = re.sub(r"```$", "", text).strip()

    return json.loads(text)


def generate_outline(
    user_prompt: str,
    character: str = "",
    setting: str = "",
    tone: str = "",
    art_style: str = ""
):
    client = genai.Client(api_key=settings.gemini_api_key)

    prompt = f"""
Create a 5-panel comic story.

User idea: {user_prompt}
Character: {character}
Setting: {setting}
Tone: {tone}
Art style: {art_style}

Return ONLY valid JSON in this format:

{{
  "title": "Comic title",
  "panels": [
    {{"panel": 1, "scene": "Scene description"}},
    {{"panel": 2, "scene": "Scene description"}},
    {{"panel": 3, "scene": "Scene description"}},
    {{"panel": 4, "scene": "Scene description"}},
    {{"panel": 5, "scene": "Scene description"}}
  ]
}}
"""

    last_error = None

    models = [
        "gemini-3.8-flash",
        "gemini-3.7-flash"
    ]

    for model in models:
        for attempt in range(4):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                if not response.text:
                    raise RuntimeError("Gemini returned an empty response.")

                return extract_json(response.text)

            except Exception as e:
                last_error = e
                error_text = str(e)

                if (
                    "503" in error_text
                    or "UNAVAILABLE" in error_text
                    or "429" in error_text
                ):
                    if attempt < 3:
                        time.sleep(2 ** attempt)
                        continue

                break

    raise RuntimeError(
        f"Gemini generation failed after retries: {last_error}"
    )