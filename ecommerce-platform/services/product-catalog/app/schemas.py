from pydantic import BaseModel, Field
from typing import Optional

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    category_id: int
    sku: str = Field(..., regex=r'^[A-Z]{3}-\d{4}$')
    image_url: Optional[str] = Field(None, max_length=255)
    
    
class ProductResponse(ProductCreate):
    id: int
    class Config:
        orm_mode = True