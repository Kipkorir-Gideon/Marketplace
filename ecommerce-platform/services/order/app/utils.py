from datetime import datetime

def generate_order_id():
    """Generate a unique order ID based on the current timestamp."""
    return f"ORDER-{int(datetime.now().timestamp())}"

def validate_order_data(order_data):
    """Validate the order data before processing."""
    required_fields = ['user_id', 'product_id', 'quantity', 'shipping_address']
    for field in required_fields:
        if field not in order_data:
            raise ValueError(f"Missing required field: {field}")
    if order_data['quantity'] <= 0:
        raise ValueError("Quantity must be greater than zero.")
    # Additional validation logic can be added here

def calculate_total_price(price_per_item, quantity):
    """Calculate the total price for the order."""
    return price_per_item * quantity

def format_order_response(order):
    """Format the order response for the API."""
    return {
        "order_id": order['order_id'],
        "user_id": order['user_id'],
        "product_id": order['product_id'],
        "quantity": order['quantity'],
        "total_price": order['total_price'],
        "status": order['status'],
        "created_at": order['created_at'].isoformat()
    }