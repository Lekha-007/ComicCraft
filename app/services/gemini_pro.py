import os
import google.generativeai as genai
from app.config import settings

# Config la irunthu key edukkrom
genai.configure(api_key=settings.gemini_api_key)

def generate_story_panels(story: str):
    # Correct model name da
    model = genai.GenerativeModel("gemini-3.8-flash")
    prompt = f"""
    You are a comic writer. Based on this story: {story}
    Generate a JSON array of 5 panels: [{{"panel":1, "description":"visual description", "dialogue":"text"}}]
    """
    response = model.generate_content(prompt)
    clean_text = response.text.replace("```json", "").replace("```", "").strip()
    return clean_text

# Ithu thaan routes.py ketkura function da! Alias mathiri
def generate_story(story: str):
    return generate_story_panels(story)