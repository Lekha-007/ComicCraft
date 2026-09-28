import os
from dotenv import load_dotenv

# OneDrive problem-kaga 2 vaati load panrom
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
load_dotenv()

class Settings:
    gemini_api_key = os.getenv("GEMINI_API_KEY", "")
    hf_token = os.getenv("HF_TOKEN", "")
    # typo thiruthiten - un code la HP_TOKEN nu irunthuchu
    gemini_outline_model = "gemini-3.8-flash"
    gemini_story_model = "gemini-3.8-flash"
    image_provider = "placeholder"
    image_model_id = "stable-diffusion-v1-5/stable-diffusion-v1-5"
    host = "127.0.0.1"
    port = 8000
    debug = True

settings = Settings()