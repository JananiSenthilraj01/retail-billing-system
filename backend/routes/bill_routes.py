from fastapi import APIRouter
from pydantic import BaseModel
from database.database import SessionLocal
from models.bill import Bill, BillItem
from models.product import Product

router = APIRouter()


class BillItemRequest(BaseModel):
    product_id: int
    quantity: int


class BillRequest(BaseModel):
    customer_name: str
    items: list[BillItemRequest]


@router.post("/bills")
def create_bill(bill_data: BillRequest):
    db = SessionLocal()

    total_amount = 0
    bill_items = []

    for item in bill_data.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()

        if product is None:
            db.close()
            return {"error": f"Product with ID {item.product_id} not found"}

        if product.stock < item.quantity:
            db.close()
            return {"error": f"Not enough stock for {product.name}"}

        item_total = product.price * item.quantity
        total_amount += item_total

        product.stock -= item.quantity

        bill_items.append({
            "product_id": product.id,
            "quantity": item.quantity,
            "price": product.price
        })

    new_bill = Bill(
        customer_name=bill_data.customer_name,
        total_amount=total_amount
    )

    db.add(new_bill)
    db.commit()
    db.refresh(new_bill)

    for item in bill_items:
        new_item = BillItem(
            bill_id=new_bill.id,
            product_id=item["product_id"],
            quantity=item["quantity"],
            price=item["price"]
        )
        db.add(new_item)

    db.commit()
    db.refresh(new_bill)
    db.close()

    return {
        "bill_id": new_bill.id,
        "customer_name": new_bill.customer_name,
        "total_amount": new_bill.total_amount
    }