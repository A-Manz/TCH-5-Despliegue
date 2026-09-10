from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
import pandas as pd
from app import model
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


@app.post("/predict", response_model=Prediccion)
def predict(vivienda: Vivienda):
    X = pd.DataFrame([vivienda.model_dump()])
    X = X.reindex(columns=model.COLUMNS, fill_value=0)
    prediccion = int(model.model.predict(X)[0])
    return Prediccion(precio_estimado=prediccion)