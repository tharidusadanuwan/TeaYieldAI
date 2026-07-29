from sqlalchemy import Column, Integer, String, Date, Numeric, Text, DateTime
from database import Base
from datetime import datetime

from sqlalchemy.orm import relationship


class TeaField(Base):

    __tablename__ = "tea_fields"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    field_name = Column(
        String(100),
        nullable=False
    )


    field_code = Column(
        String(50),
        unique=True,
        nullable=False
    )


    location = Column(
        String(150),
        nullable=False
    )


    area_size = Column(
        Numeric(10,2),
        nullable=False
    )


    tea_variety = Column(
        String(100),
        nullable=False
    )


    plantation_date = Column(
        Date
    )


    soil_type = Column(
        String(100)
    )


    altitude = Column(
        Numeric(10,2)
    )


    status = Column(
        String(50),
        default="Active"
    )


    description = Column(
        Text
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    risk_analysis = relationship(
    "RiskAnalysis",
    back_populates="field",
    cascade="all, delete"
)