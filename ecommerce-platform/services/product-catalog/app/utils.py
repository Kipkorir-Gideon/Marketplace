def validate_product_data(product_data):
    # Validate product data before creating or updating a product
    if not isinstance(product_data.get('name'), str) or not product_data['name']:
        raise ValueError("Product name must be a non-empty string.")
    if not isinstance(product_data.get('description'), str):
        raise ValueError("Product description must be a string.")
    if not isinstance(product_data.get('price'), (int, float)) or product_data['price'] < 0:
        raise ValueError("Product price must be a non-negative number.")
    if not isinstance(product_data.get('stock'), int) or product_data['stock'] < 0:
        raise ValueError("Product stock must be a non-negative integer.")
    # Additional validations can be added as needed

def format_product_response(product):
    # Format the product data for API response
    return {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock,
        "images": product.images
    }