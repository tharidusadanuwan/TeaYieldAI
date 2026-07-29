import os
import gc

import torch

torch.set_num_threads(1)

from torchvision import transforms

from PIL import Image


from .disease_model import DiseaseModel





# =====================================
# Paths
# =====================================


BASE_DIR = os.path.dirname(__file__)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "disease_model.pth"
)





# =====================================
# Lazy Model Loading
# =====================================


model = None

CLASS_NAMES = None





def get_model():


    global model

    global CLASS_NAMES



    if model is None:


        try:


            print(
                "Loading Disease AI Model..."
            )



            checkpoint = torch.load(

                MODEL_PATH,

                map_location="cpu"

            )



            CLASS_NAMES = checkpoint["classes"]



            print(
                "Loaded Disease Classes:",
                CLASS_NAMES
            )



            model = DiseaseModel(

                num_classes=len(CLASS_NAMES)

            )



            model.load_state_dict(

                checkpoint["model"]

            )



            model.eval()



            print(
                "Disease Model Loaded Successfully"
            )



        except Exception as error:


            print(
                "Disease Model Loading Error:",
                error
            )


            raise error




    return model







# =====================================
# Image Transformation
# =====================================


transform = transforms.Compose([


    transforms.Resize(

        (224,224)

    ),



    transforms.ToTensor(),



    transforms.Normalize(

        mean=[

            0.485,

            0.456,

            0.406

        ],


        std=[

            0.229,

            0.224,

            0.225

        ]

    )


])










# =====================================
# Disease Prediction
# =====================================


def predict_disease(

    image_path:str

):


    global CLASS_NAMES



    # Load model only when needed

    model = get_model()





    try:


        image = Image.open(

            image_path

        ).convert(

            "RGB"

        )



        image = transform(

            image

        )



        image = image.unsqueeze(

            0

        )





        with torch.inference_mode():



            output = model(

                image

            )



            probabilities = torch.softmax(

                output,

                dim=1

            )



            confidence, predicted = torch.max(

                probabilities,

                dim=1

            )







        disease = CLASS_NAMES[

            predicted.item()

        ]





        confidence_score = round(

            confidence.item() * 100,

            2

        )







        print(

            "Prediction:",

            disease,

            "Confidence:",

            confidence_score

        )






        return {


            "disease_name":

            disease,



            "confidence":

            confidence_score,



            "treatment":

            get_treatment(disease)


        }





    finally:


        # Clear temporary tensors

        gc.collect()











# =====================================
# Treatment Recommendation
# =====================================


def get_treatment(

    disease:str

):


    treatments = {


        "healthy":

        "No disease detected. Maintain proper fertilizer, irrigation and field monitoring.",




        "blister_blight":

        "Apply recommended fungicide, improve air circulation and remove infected leaves.",




        "brown_spot":

        "Remove infected leaves, improve soil nutrition and apply suitable fungicide.",




        "grey_blight":

        "Reduce humidity, improve field ventilation and apply fungicide.",




        "red_rust":

        "Apply copper-based fungicide and maintain proper soil nutrients."


    }





    return treatments.get(

        disease.lower(),

        "Consult agricultural expert."

    )
