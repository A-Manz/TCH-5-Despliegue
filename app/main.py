from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from app import model as ml
from app.schemas import *

app = FastAPI(
    title="APi de precios de vivienda en Madrid",
    description="Predice el precio de venta de una vivienda a partir de sus características",
    version="0.0.1"
)

@app.get("/")
def landing():
    return {
        "nombre": "API de precios de vivienda en Madrid",
        "version": "0.0.1",
        "endpoints": {
            "/": "Home. Información general",
            "/docs": "Documentación"
        }
    }