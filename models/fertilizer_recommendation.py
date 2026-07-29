from sqlalchemy import Column, Integer, String, Numeric, Text, DateTime
from database import Base
from datetime import datetime


class FertilizerRecommendation(Base):

    __tablename__ = "fertilizer_recommendations"


    recommendation_id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    field_id = Column(
        Integer,
        nullable=False
    )


    recommended_fertilizer = Column(
        String(100)
    )


    recommended_amount = Column(
        Numeric
    )


    application_time = Column(
        String(100)
    )


    reason = Column(
        Text
    )


    confidence_score = Column(
        Numeric
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )