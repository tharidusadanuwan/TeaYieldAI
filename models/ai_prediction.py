from sqlalchemy import Column, Integer, Float, String, DateTime, Date, Text

from database import Base

from datetime import datetime




class AIPrediction(Base):


    __tablename__="ai_predictions"



    prediction_id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    field_id = Column(
        Integer,
        nullable=False
    )


    prediction_date = Column(
        Date,
        nullable=False
    )


    predicted_yield = Column(
        Float,
        nullable=False
    )


    confidence_score = Column(
        Float,
        nullable=False
    )


    risk_level = Column(
        String(50),
        nullable=False
    )


    recommendation = Column(
        Text,
        nullable=True
    )


    model_version = Column(
        String(50),
        nullable=False
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )