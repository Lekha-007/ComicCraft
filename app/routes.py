from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from app.models import PromptRequest
from app.services.story import generate_outline
from app.services.image_gen import generate_panels

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate")
async def generate(
    character: str = Form(...),
    setting: str = Form(...),
    mood: str = Form(...),
    style: str = Form(...),
    story_idea: str = Form(...)
):
    data = PromptRequest(
        character=character,
        setting=setting,
        mood=mood,
        style=style,
        story_idea=story_idea
    )
    outline = generate_outline(data)
    images = generate_panels(outline, data.style)
    return JSONResponse({"outline": outline, "images": images})