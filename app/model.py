import joblib
import pandas as pd


model = joblib.load("modelo/catboost_madrid.joblib")

COLUMNS = model.regressor_.feature_names_