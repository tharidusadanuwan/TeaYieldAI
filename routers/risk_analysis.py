from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session


from database import get_db


from models.risk_analysis import RiskAnalysis


from services.risk_analysis_service import (
    analyze_field_risk,
    get_latest_risk,
    get_risk_history,
    delete_risk
)





router = APIRouter(

    prefix="/api/risk",

    tags=[
        "AI Risk Analysis"
    ]

)









# =====================================
# GET Latest Risk Analysis
# Dashboard
# =====================================


@router.get("/latest")
def latest_risk(

    db: Session = Depends(get_db)

):


    return get_latest_risk(

        db

    )




# =====================================
# GET Latest Risk By Field
# AIFieldRisk.tsx
# =====================================


@router.get("/field/{field_id}")
def get_field_risk(

    field_id:int,

    db:Session = Depends(get_db)

):


    risk = (

        db.query(
            RiskAnalysis
        )

        .filter(
            RiskAnalysis.field_id == field_id
        )

        .order_by(
            RiskAnalysis.created_at.desc()
        )

        .first()

    )



    if not risk:


        return None




    return {


        "risk_id":

        risk.risk_id,



        "field_id":

        risk.field_id,



        "field_name":

        (

            risk.field.field_name

            if risk.field

            else

            f"Field {risk.field_id}"

        ),




        "risk_score":

        risk.risk_score,



        "risk_level":

        risk.risk_level,




        "soil_risk":

        risk.soil_risk,



        "weather_risk":

        risk.weather_risk,



        "disease_risk":

        risk.disease_risk,



        "fertilizer_risk":

        risk.fertilizer_risk,



        "recommendations":

        risk.recommendations,



        "created_at":

        risk.created_at

    }




# =====================================
# GET Risk History
# Dashboard + Table
# Includes Field Name
# =====================================


@router.get("/history")
def risk_history(

    db: Session = Depends(get_db)

):


    risks = get_risk_history(

        db

    )



    return [

        {

            "risk_id": item.risk_id,

            "field_id": item.field_id,

            "field_name":
            (
                item.field.field_name
                if item.field
                else
                f"Field {item.field_id}"
            ),


            "risk_score": item.risk_score,

            "risk_level": item.risk_level,


            "soil_risk": item.soil_risk,

            "weather_risk": item.weather_risk,

            "disease_risk": item.disease_risk,

            "fertilizer_risk": item.fertilizer_risk,


            "recommendations":
            item.recommendations,


            "created_at":
            item.created_at

        }

        for item in risks

    ]












# =====================================
# Manual Risk Analysis
# Testing Only
# =====================================


@router.post("/analyze/{field_id}")
def analyze_risk(

    field_id:int,

    db:Session = Depends(get_db)

):


    result = analyze_field_risk(

        db,

        field_id

    )


    return result












# =====================================
# Delete Risk Analysis
# =====================================


@router.delete("/{risk_id}")
def remove_risk(

    risk_id:int,

    db:Session = Depends(get_db)

):


    return delete_risk(

        risk_id,

        db

    )