import os
import shutil


from sqlalchemy.orm import Session


from models.disease_detection import DiseaseDetection


from ai.disease.predict_disease import (
    predict_disease
)





UPLOAD_DIR = "uploads/disease"



os.makedirs(

    UPLOAD_DIR,

    exist_ok=True

)







def detect_disease(

    field_id:int,

    image,

    db:Session

):



    # ==============================
    # Save uploaded image
    # ==============================


    image_path = os.path.join(

        UPLOAD_DIR,

        image.filename

    )



    with open(

        image_path,

        "wb"

    ) as buffer:


        shutil.copyfileobj(

            image.file,

            buffer

        )






    # ==============================
    # AI Prediction
    # ==============================


    prediction = predict_disease(

        image_path

    )





    disease_name = prediction["disease_name"]

    confidence = prediction["confidence"]

    treatment = prediction["treatment"]





    # ==============================
    # Treatment Recommendation
    # ==============================


    treatment = get_treatment(

        disease_name

    )








    # ==============================
    # Save Database
    # ==============================



    detection = DiseaseDetection(


        field_id=field_id,


        image_path=image_path,


        disease_name=disease_name,


        confidence_score=confidence,


        treatment=treatment


    )



    db.add(detection)


    db.commit()


    db.refresh(detection)






    return {


        "detection_id":

        detection.detection_id,


        "field_id":

        field_id,


        "disease_name":

        disease_name,


        "confidence_score":

        confidence,


        "treatment":

        treatment,


        "image_path":

        image_path,


        "detected_at":

        detection.detected_at

    }










def get_treatment(disease):



    treatments = {



        "healthy":

        "No disease detected. Continue normal field maintenance.",



        "blister_blight":

        "Apply recommended fungicide and improve field ventilation.",



        "grey_blight":

        "Remove infected leaves and apply suitable fungicide.",



        "red_rust":

        "Apply copper-based fungicide and maintain soil nutrients.",



        "brown_spot":

        "Improve plant nutrition and control moisture levels.",



        "anthracnose":

        "Use disease control fungicide and remove infected parts."

    }





    return treatments.get(

        disease.lower(),

        "Consult agricultural expert for treatment."

    )