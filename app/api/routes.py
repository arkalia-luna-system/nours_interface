from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

api_router = APIRouter()

@api_router.get("/nours-image")
async def get_nours_image():
    image_path = os.path.abspath("static/images/nours.png")  # 📌 Chemin absolu
    if os.path.exists(image_path):  
        return FileResponse(image_path)  # 📌 Envoi du fichier si trouvé
    return {"error": "Image non trouvée"}  # 📌 Erreur si absente