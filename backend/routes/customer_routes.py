from fastapi import APIRouter
from pydantic import BaseModel
from database.database import SessionLocal
from models.customer import Customer

router = APIRouter()


class CustomerRequest(BaseModel):
    name: str
    phone: str


@router.get("/customers")
def get_customers():
    db = SessionLocal()
    customers = db.query(Customer).all()
    db.close()
    return customers


@router.post("/customers")
def add_customer(customer: CustomerRequest):
    db = SessionLocal()

    new_customer = Customer(
        name=customer.name,
        phone=customer.phone
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    db.close()

    return new_customer