from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from services.fertilizer_ai_service import (
generate_fertilizer_recommendation
)



router = APIRouter(
prefix="/api/ai",
tags=["AI Fertilizer"]
)





@router.post(
"/fertilizer-recommendation"
)
def fertilizer_recommendation(

field_id:int,

db:Session=Depends(get_db)

):


    result = generate_fertilizer_recommendation(

        field_id,

        db

    )


    return result