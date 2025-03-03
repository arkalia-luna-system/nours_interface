from fastapi import FastAPI
from app.api.routes import api_router
from fastapi.staticfiles import StaticFiles

# Création de l'application FastAPI
app = FastAPI()

# Montage des routes
app.include_router(api_router)

# Montage des fichiers statiques (CSS, images, JS...)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=3502, reload=True)
