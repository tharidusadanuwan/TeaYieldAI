from sqlalchemy import Column, Integer, Numeric, String, Text, Date, DateTime, ForeignKey
from sqlalchemy.sql import func

from database import Base



class YieldRecord(Base):

    __tablename__ = "yield_records"


    yield_id = Column(
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


    harvest_date = Column(
        Date,
        nullable=False
    )


    tea_weight = Column(
        Numeric(10,2),
        nullable=False
    )


    unit = Column(
        String(20),
        default="kg"
    )


    quality_grade = Column(
        String(50)
    )


    moisture_content = Column(
        Numeric(5,2)
    )


    workers_count = Column(
        Integer
    )


    weather_condition = Column(
        String(100)
    )


    notes = Column(
        Text
    )


    created_at = Column(
        DateTime,
        server_default=func.now()
    )