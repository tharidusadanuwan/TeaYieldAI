from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from database import Base


class SoilData(Base):

    __tablename__ = "soil_data"


    soil_id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    field_id = Column(
        Integer,
        ForeignKey("tea_fields.id"),
        nullable=False
    )


    soil_type = Column(
        String(100)
    )


    ph_level = Column(
        Float
    )


    nitrogen = Column(
        Float
    )


    phosphorus = Column(
        Float
    )


    potassium = Column(
        Float
    )


    moisture = Column(
        Float
    )


    organic_matter = Column(
        Float
    )


    recorded_date = Column(
        DateTime,
        server_default=func.now()
    )