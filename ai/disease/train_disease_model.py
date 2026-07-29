import os
import torch

from torchvision import datasets, transforms
from torch.utils.data import DataLoader

from ai.disease.disease_model import DiseaseModel



BASE_DIR = os.path.dirname(__file__)


DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset"
)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "disease_model.pth"
)



transform = transforms.Compose([

    transforms.Resize(
        (224,224)
    ),

    transforms.ToTensor(),

    transforms.Normalize(

        [0.485,0.456,0.406],

        [0.229,0.224,0.225]

    )

])





dataset = datasets.ImageFolder(

    DATASET_PATH,

    transform=transform

)



classes = dataset.classes



print(
    "Classes:",
    classes
)



loader = DataLoader(

    dataset,

    batch_size=16,

    shuffle=True

)





model = DiseaseModel(

    len(classes)

)



device = (

    "cuda"

    if torch.cuda.is_available()

    else

    "cpu"

)



model.to(device)




criterion = torch.nn.CrossEntropyLoss()



optimizer = torch.optim.Adam(

    model.parameters(),

    lr=0.0001

)






epochs = 20



for epoch in range(epochs):


    total_loss = 0



    for images,labels in loader:


        images = images.to(device)

        labels = labels.to(device)



        optimizer.zero_grad()



        output = model(images)



        loss = criterion(

            output,

            labels

        )



        loss.backward()



        optimizer.step()



        total_loss += loss.item()



    print(

        f"Epoch {epoch+1}/{epochs}",

        total_loss

    )







torch.save(

    {

    "model":

    model.state_dict(),


    "classes":

    classes

    },

    MODEL_PATH

)



print(
    "Disease model saved"
)