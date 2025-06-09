import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_and_get_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create product
        response = await ac.post("/products/", json={
            "name": "Test Product",
            "description": "A test product",
            "price": 9.99,
            "stock": 10,
            "image_url": "http://example.com/image.jpg"
        })
        assert response.status_code ==200
        data = response.json()
        assert data["name"] == "Test Product"
        
        # Get product
        product_id = data["id"]
        response = await ac.get(f"/products/{product_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == product_id