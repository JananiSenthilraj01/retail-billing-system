from database.database import SessionLocal
from models.store import Store


db = SessionLocal()

stores = [
    Store(
        name="RetailNova Central",
        location="Udumalpet"
    ),
    Store(
        name="RetailNova Market",
        location="Pollachi"
    ),
    Store(
        name="RetailNova City",
        location="Coimbatore"
    ),
    Store(
        name="RetailNova Express",
        location="Palakkad"
    )
]

for store in stores:
    db.add(store)

db.commit()

print("4 stores added successfully!")

db.close()