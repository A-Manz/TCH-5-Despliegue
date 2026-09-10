from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from typing import Literal
import pandas as pd
from app import model
from app.schemas import *

app = FastAPI(
    title="Tasador de precios de vivienda en venta en Madrid",
    description="Predice el precio de venta de una vivienda a partir de sus características",
    version="0.0.1"
)

### HOME
@app.get("/")
def home():
    return {
        "nombre": "Tasador de precios de vivienda en venta en Madrid",
        "version": "0.0.1",
        "descripcion": "Predice el precio de venta de una vivienda en Madrid a partir de sus caracteristicas.",
        "endpoints": {
            "/": "Informacion general.",
            "/predict": "POST. Recibe los datos de una vivienda en formato JSON y devuelve el precio estimado en euros.",
            "/docs": "Documentación interactiva. Permite probar la API desde el navegador."
        },
        "campos_obligatorios": [
            "metros", "habitaciones_limpio", "baños_limpio", "zona", "barrio", "tipo_inmueble",
            "planta_limpio", "ascensor_limpio", "localizacion_limpio"
        ]
    }


### PREDICT GET
@app.get("/predict", response_model=Prediccion)
def predict_get(
    metros: float,
    habitaciones_limpio: int,
    baños_limpio: int,
    zona: ZONAS,
    barrio: BARRIOS,
    tipo_inmueble: TIPOS_INMUEBLE,
    planta_limpio: PLANTAS,
    ascensor_limpio: Literal["S", "N", "NO_APLICA", "DESCONOCIDO"],
    localizacion_limpio: Literal["EXTERIOR", "INTERIOR", "NO_APLICA", "DESCONOCIDO"],
):

    vivienda = Vivienda(
        metros=metros,
        habitaciones_limpio=habitaciones_limpio,
        baños_limpio=baños_limpio,
        zona=zona,
        barrio=barrio,
        tipo_inmueble=tipo_inmueble,
        planta_limpio=planta_limpio,
        ascensor_limpio=ascensor_limpio,
        localizacion_limpio=localizacion_limpio,
    )
    return predict(vivienda)


### PREDICT POST
@app.post("/predict", response_model=Prediccion)
def predict(vivienda: Vivienda):
    X = pd.DataFrame([vivienda.model_dump()])
    X = X.reindex(columns=model.COLUMNS, fill_value=0)
    prediccion = int(model.model.predict(X)[0])
    return Prediccion(precio_estimado=prediccion)



### Endpoint de testeo para pedir los valores de las columnas categóricas

# @app.get("/categoricas")
# def categoricas():
#     """Devuelve los valores de las columnas categóricas"""
#     return {
#         "zonas": list(ZONAS.__args__),
#         "tipos_inmueble": list(TIPOS_INMUEBLE.__args__),
#         "plantas": list(PLANTAS.__args__),
#         "barrios": list(BARRIOS.__args__),
#     }