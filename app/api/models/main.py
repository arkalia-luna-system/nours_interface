
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.models.requestmodel import RequestModel

app = FastAPI()

def generate_response(input_text: str) -> str:
    return "Réponse générée pour : " + input_text

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/generate/")
def generate(request: RequestModel):
    response = generate_response(request.input_text)
    return {"response": response}
