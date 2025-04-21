inventory = []

def add_product(product_id, name, price, quantity, logic_expression):
    """Add a new product to the inventory."""
    product = {
        'id': product_id,
        'name': name,
        'price': price,
        'quantity': quantity,
        'logic': logic_expression  # Added logic expression field
    }
    inventory.append(product)
    print(f"✅ Product '{name}' added successfully!")

def delete_product(product_id):
    """Delete a product from the inventory by ID."""
    for i, product in enumerate(inventory):
        if product['id'] == product_id:
            del inventory[i]
            print(f"🗑️ Product with ID {product_id} deleted successfully!")
            return True
    print(f"❌ Product with ID {product_id} not found!")
    return False

def list_products():
    """Display all products in the inventory."""
    if not inventory:
        print("📦 Inventory is empty!")
        return

    print("\n📋 Current Inventory:")
    print("-" * 60)
    print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Qty':<10} {'Logic':<15}")
    print("-" * 60)

    for product in inventory:
        print(f"{product['id']:<5} {product['name']:<20} ${product['price']:<9.2f} {product['quantity']:<10} {product['logic']:<15}")
    print("-" * 60)

def save_inventory():
    """Save the inventory list to a text file."""
    with open("inventory_data.txt", "w") as file:
        for product in inventory:
            file.write(f"{product['id']}|{product['name']}|{product['price']}|{product['quantity']}|{product['logic']}\n")

def load_inventory():
    """Load the inventory from a text file."""
    inventory.clear()
    try:
        with open("inventory_data.txt", "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 5:
                    product = {
                        'id': int(parts[0]),
                        'name': parts[1],
                        'price': float(parts[2]),
                        'quantity': int(parts[3]),
                        'logic': parts[4]
                    }
                    inventory.append(product)
    except FileNotFoundError:
        print("📁 No saved inventory found. Starting fresh.")
