import joblib
import pandas as pd
from app.schemas import PLANTAS_STR


model = joblib.load("modelo/catboost_madrid.joblib")

COLUMNS = model.regressor_.feature_names_