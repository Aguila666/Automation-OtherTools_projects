from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from typing import Literal
from pathlib import Path
import logging


# Load model once at startup


class CarManufacturingClean(BaseModel):
    Defects: int = Field(gt=-1)
    Engine_Type: Literal["Electric","V6","V8"]
    Production_Line: Literal["Line 1","Line 2","Line 3"]
    
    
    
app = FastAPI(title= "Project1 Automotive Industry / Car Manufacturing API")

# ==========================
# Paths
# ==========================


BASE_DIR = Path(__file__).resolve().parent.parent.parent

LOG_DIR = BASE_DIR / "Project1_AutomotiveIndustry" / "Car_Manufacturing" / "01_Spanish" / "logs"

LOG_FILE = LOG_DIR / "api.log"

RANDOM_FOREST_PATH = BASE_DIR / "Project1_AutomotiveIndustry" / "Car_Manufacturing" / "01_Spanish" / "models" / "random_forest_baseline.joblib"

LINEAR_REGRESSION_PATH = BASE_DIR / "Project1_AutomotiveIndustry" / "Car_Manufacturing" / "01_Spanish" / "models" / "baseline_linear_regression.joblib"

# Creating necessary folders

LOG_DIR.mkdir(parents=True, exist_ok=True)

# ==========================
# Logging
# ==========================


logging.basicConfig(
	filename=LOG_FILE,
	level=logging.INFO,
	format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Starting FastAPI application initialization")


try:


    logging.info("Loading prediction models")

    model_RF = joblib.load(RANDOM_FOREST_PATH)
    model_LR = joblib.load(LINEAR_REGRESSION_PATH)


    logging.info("Prediction models loaded successfully")



    @app.get("/health")
    async def health_check():
    
        logging.info("Received GET /health request")
    
    
        logging.info("GET /health request completed successfully")
    
        return {"status": "healthy"}



    logging.info("Registering prediction endpoint")

    @app.post("/predict")
    def predict(data: CarManufacturingClean):
    
        logging.info("Received POST /predict request")

        try:

            features = [[
                data.Defects,
                int(data.Engine_Type == "V6"),
                int(data.Engine_Type == "V8"),
                int(data.Production_Line == "Line 2"),
                int(data.Production_Line == "Line 3")
            ]]
    
    
    
            features_1 = pd.DataFrame(
                features, 
                columns=[
                    "Defects", 
                    "Engine_Type_V6", 
                    "Engine_Type_V8", 
                    "Production_Line_Line 2", 
                    "Production_Line_Line 3"
                ]
            )
    
            prediction_RF = model_RF.predict(features_1)
            prediction_LR = model_LR.predict(features_1)
    
            logging.info("POST /predict request completed successfully")
    
            return {
            "predicted_Random_Forest": round(prediction_RF[0], 2), "predicted_Linear_Regression": round(prediction_LR[0], 2)
            }
    

        except Exception:
        
            logging.exception("Prediction request failed")
        
            raise

    
except Exception:
    
    logging.exception("FastAPI application initialization failed")
    
    raise