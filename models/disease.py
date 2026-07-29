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

    __tablename__ = "disease_detection"


    disease_id = Column(
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


    disease_name = Column(
        String(150),
        nullable=False
    )


    detection_date = Column(
        DateTime,
        server_default=func.now()
    )


    severity = Column(
        String(50)
    )


    confidence_score = Column(
        Float
    )


    affected_area = Column(
        Float
    )


    treatment = Column(
        Text
    )


    symptoms = Column(
        Text
    )


    image_url = Column(
        Text
    )


    notes = Column(
        Text
    )