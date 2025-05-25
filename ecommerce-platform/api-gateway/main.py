from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Microservice URLs
PRODUCT_CATALOG_URL = "http://product-catalog-service:8000"
USER_MANAGEMENT_URL = "http://user-management-service:8000"
ORDER_SERVICE_URL = "http://order-service:8000"
PAYMENT_SERVICE_URL = "http://payment-service:3000"

@app.get("/")
async def root():
    return {"message": "Welcome to the E-Commerce API Gateway"}

@app.get("/products")
async def get_products():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PRODUCT_CATALOG_URL}/products")
        return response.json()

@app.post("/register")
async def register_user(user: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USER_MANAGEMENT_URL}/register", json=user)
        return response.json()

@app.post("/orders")
async def create_order(order: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{ORDER_SERVICE_URL}/orders", json=order)
        return response.json()

@app.post("/payments")
async def process_payment(payment: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{PAYMENT_SERVICE_URL}/payments", json=payment)
        return response.json()