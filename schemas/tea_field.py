from pydantic import BaseModel
from datetime import date


class TeaFieldCreate(BaseModel):

    field_name:str
    field_code:str
    location:str
    area_size:float
    tea_variety:str
    plantation_date:date
    soil_type:str
    altitude:float
    status:str
    description:str



class TeaFieldUpdate(TeaFieldCreate):
    pass