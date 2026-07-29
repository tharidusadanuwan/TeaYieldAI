from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db


from models.tea_field import TeaField
from models.yield_record import YieldRecord
from models.risk_analysis import RiskAnalysis
from models.ai_prediction import AIPrediction


from sqlalchemy import extract


router = APIRouter(

    prefix="/api/dashboard",

    tags=[
        "Dashboard"
    ]

)









@router.get("/summary")
def dashboard_summary(

    db:Session = Depends(get_db)

):


    total_fields = db.query(
        TeaField
    ).count()






    # Real Harvest Data

    yields = db.query(
        YieldRecord
    ).all()



    monthly_harvest = sum(

        float(item.tea_weight or 0)

        for item in yields

    )







    # AI Predicted Yield

    latest_prediction = (

        db.query(AIPrediction)

        .order_by(

            AIPrediction.created_at.desc()

        )

        .first()

    )



    expected_yield = (

        float(
            latest_prediction.predicted_yield
        )

        if latest_prediction

        else 0

    )







    # Risk Score

    latest_risk = (

        db.query(RiskAnalysis)

        .order_by(

            RiskAnalysis.created_at.desc()

        )

        .first()

    )



    return {


        "total_fields":

        total_fields,



        "monthly_harvest":

        monthly_harvest,



        "expected_yield":

        expected_yield,



        "risk_score":

        latest_risk.risk_score

        if latest_risk

        else 0


    }



@router.get("/yield-comparison")
def yield_comparison(

    db:Session = Depends(get_db)

):


    predictions = db.query(
        AIPrediction
    ).all()



    result = []



    for prediction in predictions:


        field = db.query(

            TeaField

        ).filter(

            TeaField.id == prediction.field_id

        ).first()



        field_name = (

            field.field_name

            if field

            else

            f"Field {prediction.field_id}"

        )



        harvest = db.query(

            YieldRecord

        ).filter(

            YieldRecord.field_id == prediction.field_id

        ).all()



        actual_yield = sum(

            float(item.tea_weight or 0)

            for item in harvest

        )



        result.append({

            "field_name":

            field_name,


            "predicted_yield":

            float(prediction.predicted_yield),



            "actual_yield":

            actual_yield

        })



    return result



@router.get("/monthly-harvest")
def monthly_harvest(

    db:Session = Depends(get_db)

):


    records = db.query(
        YieldRecord
    ).all()



    months = {}


    for item in records:


        month = item.harvest_date.strftime("%b")


        if month not in months:

            months[month]=0



        months[month] += float(
            item.tea_weight or 0
        )



    return [

        {
            "month":key,
            "harvest":value
        }

        for key,value in months.items()

    ]


@router.get("/risk-overview")
def risk_overview(

    db:Session = Depends(get_db)

):


    latest = db.query(

        RiskAnalysis

    ).order_by(

        RiskAnalysis.created_at.desc()

    ).first()



    if not latest:

        return []



    return [

        {
            "risk":"Soil",
            "value":float(latest.soil_risk)
        },

        {
            "risk":"Weather",
            "value":float(latest.weather_risk)
        },


        {
            "risk":"Disease",
            "value":float(latest.disease_risk)
        },


        {
            "risk":"Fertilizer",
            "value":float(latest.fertilizer_risk)
        },


        {
            "risk":"Overall",
            "value":float(latest.risk_score)
        }

    ]