from pydantic import BaseModel
from typing import Optional


class PromptRequest(BaseModel):
    prompt: str
    character: Optional[str] = ""
    setting: Optional[str] = ""
    tone: Optional[str] = ""
    art_style: Optional[str] = ""


class Panel(BaseModel):
    panel_number: int
    scene: str
    caption: str = ""
    dialogue: str = ""
    narration: str = ""
    image_path: str = ""


class ComicResponse(BaseModel):
    title: str
    panels: list[Panel]