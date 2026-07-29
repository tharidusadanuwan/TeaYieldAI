from pydantic import BaseModel



class FertilizerRecommendationRequest(BaseModel):

    field_id:int





class FertilizerRecommendationResponse(BaseModel):

    fertilizer:str

    amount:float

    application_time:str

    confidence:float

    reason:str