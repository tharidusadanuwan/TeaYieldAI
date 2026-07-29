from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.sql import func

from database import Base



class DiseaseDetection(Base):

    __tablename__ = "ai_disease_detection"



    detection_id = Column(

        Integer,

        primary_key=True,

        index=True

    )



    field_id = Column(

        Integer,

        ForeignKey(
            "tea_fields.id",
            ondelete="CASCADE"
        ),

        nullable=False

    )



    image_path = Column(

        String(255)

    )



    disease_name = Column(

        String(100)

    )



    confidence_score = Column(

        Float

    )



    treatment = Column(

        Text

    )



    detected_at = Column(

        DateTime,

        server_default=func.now()

    )