from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import os

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent.parent

# folder irukka nu check panni mount panrom
if not os.path.exists("app/static"):
    os.makedirs("app/static", exist_ok=True)
if not os.path.exists("panels"):
    os.makedirs("panels", exist_ok=True)

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/panels", StaticFiles(directory="panels"), name="panels")

from app.routes import router
app.include_router(router)