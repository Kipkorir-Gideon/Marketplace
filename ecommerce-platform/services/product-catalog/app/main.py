from fastapi import FastAPI

from .routes import router as product_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Product Catalog Service!"}
