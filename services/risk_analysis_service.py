from sqlalchemy.orm import Session


from models.risk_analysis import RiskAnalysis


from models.soil import SoilData


from models.weather import WeatherData


from models.disease_detection import DiseaseDetection


from models.fertilizer import FertilizerUsage





from datetime import datetime







# =====================================
# Main Risk Analysis Function
# =====================================


def analyze_field_risk(
    
    db: Session,

    field_id:int

):


    # -----------------------------
    # Get Existing Data
    # -----------------------------


    soil = db.query(

        SoilData

    ).filter(

        SoilData.field_id == field_id

    ).order_by(

        SoilData.recorded_date.desc()

    ).first()





    weather = db.query(
    WeatherData
).filter(
    WeatherData.field_id == field_id
).order_by(
    WeatherData.recorded_date.desc()
).first()





    disease = db.query(

        DiseaseDetection

    ).filter(

        DiseaseDetection.field_id == field_id

    ).order_by(

        DiseaseDetection.detected_at.desc()

    ).first()





    fertilizer = db.query(
    FertilizerUsage
).filter(
    FertilizerUsage.field_id == field_id
).order_by(
    FertilizerUsage.application_date.desc()
).first()









    # -----------------------------
    # Calculate Individual Risks
    # -----------------------------


    soil_risk = calculate_soil_risk(

        soil

    )


    weather_risk = calculate_weather_risk(

        weather

    )


    disease_risk = calculate_disease_risk(

        disease

    )


    fertilizer_risk = calculate_fertilizer_risk(

        fertilizer

    )







    # -----------------------------
    # Final Risk Score
    # -----------------------------


    risk_score = round(

        (

            soil_risk * 0.30

            +

            weather_risk * 0.25

            +

            disease_risk * 0.35

            +

            fertilizer_risk * 0.10

        ),

        2

    )





    risk_level = get_risk_level(

        risk_score

    )





    recommendations = generate_recommendations(

        soil_risk,

        weather_risk,

        disease_risk,

        fertilizer_risk

    )







    # -----------------------------
    # Save Database
    # -----------------------------


    risk = RiskAnalysis(

        field_id=field_id,

        risk_score=risk_score,

        risk_level=risk_level,

        soil_risk=soil_risk,

        weather_risk=weather_risk,

        disease_risk=disease_risk,

        fertilizer_risk=fertilizer_risk,

        recommendations=recommendations

    )




    db.add(risk)


    db.commit()


    db.refresh(risk)







    return {


        "risk_id":

        risk.risk_id,


        "field_id":

        field_id,


        "risk_score":

        risk_score,


        "risk_level":

        risk_level,


        "soil_risk":

        soil_risk,


        "weather_risk":

        weather_risk,


        "disease_risk":

        disease_risk,


        "fertilizer_risk":

        fertilizer_risk,


        "recommendations":

        recommendations,


        "created_at":

        risk.created_at

    }









# =====================================
# Soil Risk
# =====================================


def calculate_soil_risk(soil):


    if not soil:

        return 50




    risk = 0





    if soil.moisture < 30:

        risk += 40



    if soil.nitrogen < 40:

        risk += 30



    if soil.ph_level < 5 or soil.ph_level > 7:

        risk += 30




    return min(

        risk,

        100

    )









# =====================================
# Weather Risk
# =====================================


def calculate_weather_risk(weather):

    rainfall = float(weather.rainfall or 0)

    humidity = float(weather.humidity or 0)

    temperature = float(weather.temperature or 0)



    risk = 0



    # Heavy rainfall risk
    if rainfall > 100:
        risk += 40

    elif rainfall > 50:
        risk += 25



    # Dry condition risk
    elif rainfall < 5:
        risk += 25



    # High humidity disease risk
    if humidity > 85:
        risk += 30

    elif humidity > 70:
        risk += 15



    # Temperature stress
    if temperature > 32:
        risk += 20

    elif temperature < 18:
        risk += 15



    return min(risk,100)










# =====================================
# Disease Risk
# =====================================


def calculate_disease_risk(disease):


    if not disease:

        return 10




    confidence = disease.confidence_score





    if confidence > 80:

        return 90



    elif confidence > 50:

        return 60



    else:

        return 30










# =====================================
# Fertilizer Risk
# =====================================


def calculate_fertilizer_risk(fertilizer):


    if not fertilizer:

        return 50



    return 20











# =====================================
# Risk Level
# =====================================


def get_risk_level(score):


    if score >= 75:

        return "High"



    elif score >= 45:

        return "Medium"



    else:

        return "Low"









# =====================================
# Recommendations
# =====================================


def generate_recommendations(

    soil,

    weather,

    disease,

    fertilizer

):


    result=[]



    if soil > 40:

        result.append(

            "Improve soil condition and nutrient level"

        )



    if weather > 40:

        result.append(

            "Monitor weather stress conditions"

        )



    if disease > 40:

        result.append(

            "Inspect plants and control diseases"

        )



    if fertilizer > 40:

        result.append(

            "Review fertilizer application"

        )




    if not result:

        result.append(

            "Field condition is healthy"

        )





    return ", ".join(result)









# =====================================
# History
# =====================================


def get_risk_history(

    db:Session

):


    return db.query(

        RiskAnalysis

    ).order_by(

        RiskAnalysis.created_at.desc()

    ).all()






# =====================================
# Latest Risk Analysis
# =====================================


def get_latest_risk(

    db:Session

):


    return db.query(

        RiskAnalysis

    ).order_by(

        RiskAnalysis.created_at.desc()

    ).limit(5).all()






# =====================================
# Delete
# =====================================


def delete_risk(

    risk_id:int,

    db:Session

):


    risk = db.query(

        RiskAnalysis

    ).filter(

        RiskAnalysis.risk_id == risk_id

    ).first()


    if not risk:

        return {

            "message":

            "Risk record not found"

        }



    db.delete(risk)

    db.commit()


    return {


        "message":

        "Risk analysis deleted successfully"

    }