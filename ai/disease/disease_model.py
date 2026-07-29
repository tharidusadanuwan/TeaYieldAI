import torch
import torch.nn as nn
from torchvision import models



class DiseaseModel(nn.Module):


    def __init__(self, num_classes):

        super().__init__()


        self.model = models.mobilenet_v3_large(
            weights="DEFAULT"
        )


        in_features = (
            self.model.classifier[3].in_features
        )


        self.model.classifier[3] = nn.Linear(

            in_features,

            num_classes

        )



    def forward(self,x):

        return self.model(x)