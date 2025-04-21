# inventory_system.py

inventory = []

def add_product(product_id, name, price, quantity, logic):
    """Add a new product to the inventory if it doesn't already exist."""
    # Check if the product with the same ID already exists
    for product in inventory:
        if product["id"] == product_id:
            print(f"⚠️ Product with ID {product_id} already exists.")
            return  # Skip adding the product if it already exists
    
    inventory.append({"id": product_id, "name": name, "price": price, "quantity": quantity, "logic": logic})
    print(f"✅ Product '{name}' added successfully!")

def delete_product(product_id):
    """Delete a product from the inventory by its ID."""
    global inventory
    inventory = [product for product in inventory if product["id"] != product_id]
    print(f"🗑️ Product with ID {product_id} deleted successfully!")

def list_products():
    """List all products in the inventory."""
    if not inventory:
        print("No products in inventory.")
        return
    print(f"{'ID':<5}{'Name':<20}{'Price':<10}{'Qty':<10}{'Logic':<10}")
    print("-" * 55)
    for product in inventory:
        print(f"{product['id']:<5}{product['name']:<20}{product['price']:<10}{product['quantity']:<10}{product['logic']:<10}")

def save_inventory(file_name="inventory_data.txt"):
    """Save the inventory to a text file."""
    with open(file_name, "w") as file:
        for product in inventory:
            file.write(f"{product['id']}|{product['name']}|{product['price']}|{product['quantity']}|{product['logic']}\n")
    print(f"✅ Inventory saved to {file_name}!")

def load_inventory(file_name="inventory_data.txt"):
    """Load the inventory from a text file."""
    global inventory
    inventory.clear()  # Clear the existing inventory to prevent duplicates
    try:
        with open(file_name, "r") as file:
            for line in file:
                product_data = line.strip().split("|")
                product_id, name, price, quantity, logic = product_data
                inventory.append({
                    "id": int(product_id),
                    "name": name,
                    "price": float(price),
                    "quantity": int(quantity),
                    "logic": logic
                })
        print(f"✅ Inventory loaded from {file_name}!")
    except FileNotFoundError:
        print(f"⚠️ {file_name} not found. Starting with an empty inventory.")
