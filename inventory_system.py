inventory = []

def load_inventory(filename="inventory_data.txt"):
    """Load inventory from a text file."""
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 5:  # Ensure correct data format
                    product = {
                        "id": int(parts[0]),
                        "name": parts[1],
                        "price": float(parts[2]),
                        "quantity": int(parts[3]),
                        "logic": parts[4]
                    }
                    inventory.append(product)
        print("✅ Inventory loaded successfully!")
    except FileNotFoundError:
        print("⚠️ Inventory file not found, starting with an empty inventory.")
    except Exception as e:
        print(f"⚠️ Error loading inventory: {e}")

def save_inventory(filename="inventory_data.txt"):
    """Save inventory to a text file."""
    try:
        with open(filename, "w") as file:
            for product in inventory:
                file.write(f"{product['id']}|{product['name']}|{product['price']}|{product['quantity']}|{product['logic']}\n")
        print("✅ Inventory saved successfully!")
    except Exception as e:
        print(f"⚠️ Error saving inventory: {e}")

def add_product(id, name, price, quantity, logic):
    """Add a new product to the inventory."""
    if any(product['id'] == id for product in inventory):
        print(f"⚠️ Product with ID {id} already exists.")
    else:
        inventory.append({"id": id, "name": name, "price": price, "quantity": quantity, "logic": logic})
        print(f"✅ Product '{name}' added successfully!")
        save_inventory()  # Automatically save after adding

def delete_product(id):
    """Delete a product from the inventory by its ID."""
    global inventory
    inventory = [product for product in inventory if product["id"] != id]
    print(f"🗑️ Product with ID {id} deleted successfully!")
    save_inventory()  # Automatically save after deleting

def list_products():
    """List all products in the inventory."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return

    print("📋 Current Inventory:")
    print("------------------------------------------------------------")
    print("ID    Name                 Price      Qty        Logic")
    print("------------------------------------------------------------")
    for product in inventory:
        print(f"{product['id']}     {product['name']:20} ${product['price']:8.2f}   {product['quantity']:3}     {product['logic']}")
    print("------------------------------------------------------------")
