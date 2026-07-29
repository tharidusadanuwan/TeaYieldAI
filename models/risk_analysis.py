from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database import Base

from datetime import datetime



class RiskAnalysis(Base):

    __tablename__ = "risk_analysis"



    risk_id = Column(
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



    risk_score = Column(
        Float
    )


    risk_level = Column(
        String(50)
    )



    soil_risk = Column(
        Float
    )


    weather_risk = Column(
        Float
    )


    disease_risk = Column(
        Float
    )


    fertilizer_risk = Column(
        Float
    )


    recommendations = Column(
        Text
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )



    # Relationship

    field = relationship(
        "TeaField",
        back_populates="risk_analysis"
    )