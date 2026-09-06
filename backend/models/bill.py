from sqlalchemy import Column, Integer, Float, String, DateTime
from database.database import Base
from datetime import datetime


class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class BillItem(Base):
    __tablename__ = "bill_items"

    id = Column(Integer, primary_key=True, index=True)
    bill_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)