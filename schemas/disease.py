from pydantic import BaseModel
from datetime import datetime


class DiseaseCreate(BaseModel):

    field_id:int

    disease_name:str

    severity:str

    confidence_score:float

    affected_area:float

    treatment:str

    symptoms:str

    image_url:str | None = None

    notes:str | None = None



class DiseaseUpdate(BaseModel):

    field_id:int

    disease_name:str

    severity:str

    confidence_score:float

    affected_area:float

    treatment:str

    symptoms:str

    image_url:str | None = None

    notes:str | None = None



class DiseaseResponse(BaseModel):

    disease_id:int

    field_id:int

    disease_name:str

    detection_date:datetime

    severity:str

    confidence_score:float

    affected_area:float

    treatment:str

    symptoms:str

    image_url:str | None

    notes:str | None


    class Config:

        from_attributes=True