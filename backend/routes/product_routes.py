from fastapi import APIRouter
from pydantic import BaseModel
from database.database import SessionLocal
from models.product import Product

router = APIRouter()


class ProductRequest(BaseModel):
    name: str
    price: float
    stock: int


@router.get("/products")
def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products


@router.post("/products")
def add_product(product: ProductRequest):
    db = SessionLocal()

    new_product = Product(
        name=product.name,
        price=product.price,
        stock=product.stock
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    db.close()

    return new_product