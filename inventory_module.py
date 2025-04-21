# Initialize an empty inventory list
inventory = []

def add_product(product_id, name, price, quantity):
    """Add a new product to the inventory."""
    product = {
        'id': product_id,
        'name': name,
        'price': price,
        'quantity': quantity
    }
    inventory.append(product)
    print(f"Product '{name}' added successfully!")

def delete_product(product_id):
    """Delete a product from the inventory by ID."""
    for i, product in enumerate(inventory):
        if product['id'] == product_id:
            del inventory[i]
            print(f"Product with ID {product_id} deleted successfully!")
            return True
    print(f"Product with ID {product_id} not found!")
    return False

def list_products():
    """Display all products in the inventory."""
    if not inventory:
        print("Inventory is empty!")
        return
    
    print("\nCurrent Inventory:")
    print("-" * 50)
    print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Quantity':<10}")
    print("-" * 50)
    
    for product in inventory:
        print(f"{product['id']:<5} {product['name']:<20} ${product['price']:<9} {product['quantity']:<10}")
    print("-" * 50) 