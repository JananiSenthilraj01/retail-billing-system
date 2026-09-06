import os
import json

from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv

from google import genai

from database.database import SessionLocal
from models.product import Product
from models.bill import Bill, BillItem


# ==================================================
# LOAD GEMINI API KEY FROM PROJECT ROOT .env
# ==================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_PATH)


# ==================================================
# GEMINI CLIENT
# ==================================================

api_key = os.getenv("GEMINI_API_KEY")

client = None

if api_key:
    client = genai.Client(api_key=api_key)


# ==================================================
# ROUTER
# ==================================================

router = APIRouter()


# ==================================================
# REQUEST MODEL
# ==================================================

class CopilotRequest(BaseModel):
    question: str


# ==================================================
# RETAILNOVA COPILOT
# ==================================================

@router.post("/copilot")
def ask_copilot(request: CopilotRequest):

    db = SessionLocal()

    try:

        # ==================================================
        # GET INVENTORY
        # ==================================================

        products = db.query(Product).all()

        inventory_data = []

        for product in products:

            inventory_data.append({
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "stock": product.stock
            })


        # ==================================================
        # GET SALES
        # ==================================================

        bills = db.query(Bill).all()

        sales_data = []

        for bill in bills:

            sales_data.append({
                "bill_id": bill.id,
                "customer": bill.customer_name,
                "total": bill.total_amount,
                "created_at": str(bill.created_at)
            })


        # ==================================================
        # GET SOLD ITEMS
        # ==================================================

        bill_items = db.query(BillItem).all()

        sold_items_data = []

        for item in bill_items:

            sold_items_data.append({
                "bill_id": item.bill_id,
                "product_id": item.product_id,
                "quantity": item.quantity,
                "price": item.price
            })


        # ==================================================
        # CLOSE DATABASE
        # ==================================================

        db.close()


        # ==================================================
        # CHECK GEMINI
        # ==================================================

        if client is None:

            return {
                "answer":
                    "Gemini is not configured. "
                    "Please check GEMINI_API_KEY "
                    "in the project .env file."
            }


        # ==================================================
        # PREPARE RETAIL DATA
        # ==================================================

        retail_data = {
            "inventory": inventory_data,
            "sales": sales_data,
            "sold_items": sold_items_data
        }


        # ==================================================
        # AI PROMPT
        # ==================================================

        prompt = f"""
You are RetailNova AI, an intelligent retail
sales and inventory copilot for store managers.

The manager asked:

"{request.question}"

Here is the REAL retail data from the database:

{json.dumps(retail_data, indent=2)}

IMPORTANT RULES:

1. Use ONLY the retail data provided above.

2. Never invent products, sales, customers,
   quantities, prices, or other business data.

3. If information is unavailable, clearly say:
   "The data is not available."

4. Give practical business advice.

5. Keep the answer easy for a store manager
   to understand.

6. Use short sections and bullet points.

7. When discussing inventory, mention the
   actual stock quantity.

8. When discussing sales, use the actual
   recorded sales.

9. If stock is low, recommend restocking.

10. If sales are strong, explain what the
    manager should do next.

11. Do not claim to have information that
    is not present in the database.

12. Keep the response concise but useful.

Answer using this format when appropriate:

📊 Business Insight

📦 Inventory
- ...

💰 Sales
- ...

🎯 Recommended Action
- ...
"""


        # ==================================================
        # SEND REQUEST TO GEMINI 3.5 FLASH
        # ==================================================

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )


        # ==================================================
        # GET AI RESPONSE
        # ==================================================

        answer = response.text


        # ==================================================
        # RETURN RESPONSE
        # ==================================================

        return {
            "answer": answer,
            "question": request.question,
            "data_used": {
                "products": len(inventory_data),
                "bills": len(sales_data),
                "sold_items": len(sold_items_data)
            }
        }


    # ==================================================
    # ERROR HANDLING
    # ==================================================

    except Exception as e:

        try:
            db.close()
        except Exception:
            pass

        print(
            "Gemini Copilot Error:",
            str(e)
        )

        return {
            "answer":
                "⚠️ RetailNova Copilot could not "
                "connect to Gemini right now. "
                "Please check the backend terminal.",

            "error": str(e)
        }