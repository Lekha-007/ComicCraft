import pathlib
code = """import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
OUTLINE_MODEL = os.getenv("GEMINI_OUTLINE_MODEL", "gemini-3.8-flash")
STORY_MODEL = os.getenv("GEMINI_STORY_MODEL", "gemini-3.8-flash")

def generate_outline(user_prompt: str):
    prompt = f"You are a comic outline generator. Idea: {user_prompt}. Create 4 scenes JSON array like [{{\\"scene\\":1, \\"description\\":\\"cute fox...\\"}}]"
    response = client.models.generate_content(model=OUTLINE_MODEL, contents=prompt)
    text = response.text.strip()
    bq = chr(96)*3
    if bq in text:
        parts = text.split(bq)
        if len(parts) >= 2:
            text = parts[1].replace("json","").strip()
    try:
        return json.loads(text)
    except:
        return [{"scene": 1, "description": text}]

def generate_story_panel(scene_desc: str):
    prompt = f"Write a short cute comic panel story for: {scene_desc}. Keep it fun, anime fox."
    response = client.models.generate_content(model=STORY_MODEL, contents=prompt)
    return response.text.strip()
"""
pathlib.Path("app/services/gemini_flash.py").write_text(code, encoding="utf-8")
print("FIXED DA!")