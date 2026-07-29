from pydantic import BaseModel

from datetime import date, datetime

from typing import Optional




class AIPredictionCreate(BaseModel):

    field_id:int

    prediction_date:date

    predicted_yield:float

    confidence_score:float

    risk_level:str

    recommendation:str

    model_version:str




class AIPredictionResponse(AIPredictionCreate):

    prediction_id:int

    created_at:Optional[datetime] = None



    class Config:

        from_attributes=True