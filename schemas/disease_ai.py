from pydantic import BaseModel
from datetime import datetime



class DiseaseDetectionResponse(BaseModel):

    detection_id:int

    field_id:int

    disease_name:str

    confidence_score:float

    treatment:str

    image_path:str

    detected_at:datetime



    class Config:

        from_attributes = True