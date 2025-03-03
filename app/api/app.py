from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import api_router

app = FastAPI()

# 📌 Montage du dossier 'static' pour servir les images
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 📌 Inclusion des routes de l'API
app.include_router(api_router)