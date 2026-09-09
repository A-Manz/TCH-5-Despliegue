"""
API con FastAPI - Modelo de predicción de vivienda en venta en Madrid
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
import joblib
import pandas as pd
import os