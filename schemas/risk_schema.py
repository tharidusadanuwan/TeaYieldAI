from pydantic import BaseModel

from datetime import datetime




# =====================================
# Response Schema
# =====================================


class RiskAnalysisResponse(BaseModel):

    risk_id:int

    field_id:int

    field_name:str

    risk_score:float

    risk_level:str

    soil_risk:float

    weather_risk:float

    disease_risk:float

    fertilizer_risk:float

    recommendations:str

    created_at:datetime


    class Config:
        from_attributes=True






# =====================================
# Prediction Request Schema
# =====================================


class RiskPredictionRequest(BaseModel):


    nitrogen:float


    phosphorus:float


    potassium:float


    moisture:float


    ph_level:float


    temperature:float


    humidity:float


    rainfall:float


    disease_score:float


    fertilizer_days:int