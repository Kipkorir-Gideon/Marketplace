from fastapi import FastAPI
from routes import router as order_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Middleware to allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the order routes
app.include_router(order_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Order Service!"}