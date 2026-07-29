from pydantic import BaseModel

from datetime import datetime



class FertilizerCreate(BaseModel):

    field_id:int

    fertilizer_type:str

    application_method:str

    quantity:float

    unit:str

    nitrogen_content:float

    phosphorus_content:float

    potassium_content:float

    notes:str | None = None





class FertilizerUpdate(BaseModel):

    field_id:int

    fertilizer_type:str

    application_method:str

    quantity:float

    unit:str

    nitrogen_content:float

    phosphorus_content:float

    potassium_content:float

    notes:str | None = None





class FertilizerResponse(BaseModel):

    fertilizer_id:int

    field_id:int

    fertilizer_type:str

    application_method:str

    quantity:float

    unit:str

    application_date:datetime

    nitrogen_content:float

    phosphorus_content:float

    potassium_content:float

    notes:str | None


    class Config:

        from_attributes=True