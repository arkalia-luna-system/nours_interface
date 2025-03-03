from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/nours-image")
async def get_nours_image():
    image_path = os.path.join("static", "images", "nours.png")
    return FileResponse(image_path)