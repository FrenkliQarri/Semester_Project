inventory = []

def load_inventory(filename="inventory_data.txt"):
    """Load inventory data from a file."""
    try:
        with open(filename, "r") as file:
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
        print("✅ Inventory loaded successfully!")
    except FileNotFoundError:
        print("⚠️ Inventory file not found. Starting with an empty inventory.")
    except Exception as e:
        print(f"⚠️ Error loading inventory: {e}")

def save_inventory(filename="inventory_data.txt"):
    """Save inventory data to a file."""
    try:
        with open(filename, "w") as file:
            for product in inventory:
                file.write(f"{product['id']}|{product['name']}|{product['price']}|{product['quantity']}|{product['logic']}\n")
        print("✅ Inventory saved successfully!")
    except Exception as e:
        print(f"⚠️ Error saving inventory: {e}")

def add_product():
    """Add a product to the inventory."""
    product_id = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    logic = input("Enter product logic (e.g., p1 ∧ p2): ")

    # Check if the product ID already exists
    for product in inventory:
        if product['id'] == product_id:
            print(f"⚠️ Product with ID {product_id} already exists.")
            return
    
    inventory.append({"id": product_id, "name": name, "price": price, "quantity": quantity, "logic": logic})
    print(f"✅ Product '{name}' added successfully!")

def delete_product():
    """Delete a product from the inventory."""
    product_id = int(input("Enter the product ID to delete: "))
    for product in inventory:
        if product["id"] == product_id:
            inventory.remove(product)
            print(f"🗑️ Product with ID {product_id} deleted successfully!")
            return
    print(f"⚠️ No product found with ID {product_id}.")

def list_products():
    """List all products in the inventory."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return
    print("📋 Current Inventory:")
    print("-" * 60)
    print(f"{'ID':<5}{'Name':<20}{'Price':<10}{'Qty':<10}{'Logic':<20}")
    print("-" * 60)
    for product in inventory:
        print(f"{product['id']:<5}{product['name']:<20}{product['price']:<10}{product['quantity']:<10}{product['logic']:<20}")
    print("-" * 60)
