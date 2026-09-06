from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import Base, engine, SessionLocal

from models.product import Product
from models.customer import Customer
from models.bill import Bill, BillItem
from models.store import Store

from routes.product_routes import router as product_router
from routes.customer_routes import router as customer_router
from routes.bill_routes import router as bill_router
from routes.copilot_routes import router as copilot_router


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="RetailNova",
    description="AI Sales and Inventory Copilot",
    version="1.0.0"
)


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Existing routes
app.include_router(product_router)
app.include_router(customer_router)
app.include_router(bill_router)
app.include_router(copilot_router)


# Get all stores
@app.get("/stores")
def get_stores():

    db = SessionLocal()

    stores = db.query(Store).all()

    result = []

    for store in stores:
        result.append({
            "id": store.id,
            "name": store.name,
            "location": store.location
        })

    db.close()

    return result


# Get all sales
@app.get("/sales")
def get_sales():

    db = SessionLocal()

    bills = db.query(Bill).all()

    result = []

    for bill in bills:
        result.append({
            "id": bill.id,
            "customer_name": bill.customer_name,
            "total_amount": bill.total_amount,
            "created_at": str(bill.created_at)
        })

    db.close()

    return result


# Dashboard summary
@app.get("/dashboard")
def get_dashboard():

    db = SessionLocal()

    stores = db.query(Store).count()
    products = db.query(Product).count()
    bills = db.query(Bill).all()

    total_sales = sum(
        bill.total_amount for bill in bills
    )

    db.close()

    return {
        "stores": stores,
        "products": products,
        "bills": len(bills),
        "total_sales": total_sales
    }


@app.get("/")
def home():
    return {
        "message": "RetailNova - AI Sales & Inventory Copilot is running!"
    }