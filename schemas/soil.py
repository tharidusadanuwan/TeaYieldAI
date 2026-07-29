from pydantic import BaseModel
from datetime import datetime


class SoilCreate(BaseModel):

    field_id:int

    soil_type:str

    ph_level:float

    nitrogen:float

    phosphorus:float

    potassium:float

    moisture:float

    organic_matter:float




class SoilResponse(BaseModel):

    soil_id:int

    field_id:int

    soil_type:str

    ph_level:float

    nitrogen:float

    phosphorus:float

    potassium:float

    moisture:float

    organic_matter:float

    recorded_date:datetime


    class Config:

        from_attributes=True