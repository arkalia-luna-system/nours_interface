from fastapi import FastAPI
from app.api.main import app
from fastapi.responses import HTMLResponse, FileResponse
import os


@app.get("/nours-image")
async def get_nours_image():
    image_path = os.path.join("static", "images", "nours.png")
    return FileResponse(image_path)