from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
from .database import Base


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    image_url: Optional[str] = None


class ProductORM(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    image_url = Column(String)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
