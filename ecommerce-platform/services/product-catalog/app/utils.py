from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from .database import SessionLocal
from .models import ProductORM, ProductCreate, ProductUpdate


# Create a new product
async def create_product(product: ProductCreate):
    async with SessionLocal() as session:
        db_product = ProductORM(**product.dict())
        session.add(db_product)
        await session.commit()
        await session.refresh(db_product)
        return db_product


# Get a list of products (with pagination)
async def get_product(skip: int = 0, limit: int = 10):
    async with SessionLocal() as session:
        result = await session.execute(select(ProductORM).offset(skip).limit(limit))
        return result.scalars().all()


# get a single product by ID
async def get_product_by_id(product_id: int):
    async with SessionLocal() as session:
        result = await session.execute(
            select(ProductORM).where(ProductORM.id == product_id)
        )
        product = result.scale_one_or_none()
        return product


# Update a product
async def update_product(product_id: int, product: ProductUpdate):
    async with SessionLocal() as session:
        result = await session.execute(
            select(ProductORM).where(ProductORM.id == product_id)
        )
        db_product = result.scalar_one_or_none()
        if not db_product:
            return None
        for key, value in product.dict(exclude_unset=True).items():
            setattr(db_product, key, value)
        await session.commit()
        await session.refresh(db_product)
        return db_product


# Delete a product
async def delete_product(product_id: int):
    async with SessionLocal() as session:
        result = await session.execute(
            select(ProductORM).where(ProductORM.id == product_id)
        )
        db_product = result.scalar_one_or_none()
        if not db_product:
            return False
        await session.delete(db_product)
        await session.commit()
        return True
