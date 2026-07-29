from pydantic import BaseModel
from datetime import date
from typing import Optional



class YieldRecordCreate(BaseModel):

    field_id:int

    harvest_date:date

    tea_weight:float

    unit:str

    quality_grade:Optional[str]=None

    moisture_content:Optional[float]=None

    workers_count:Optional[int]=None

    weather_condition:Optional[str]=None

    notes:Optional[str]=None





class YieldRecordUpdate(YieldRecordCreate):

    pass