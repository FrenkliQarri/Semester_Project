inventory = []

def add_product(product_id, name, price, quantity, logic):
    product = {
        'id': product_id,
        'name': name,
        'price': price,
        'quantity': quantity,
        'logic': logic
    }
    inventory.append(product)
    print(f"✅ Product '{name}' added successfully!")

def delete_product(product_id):
    global inventory
    inventory = [p for p in inventory if p['id'] != product_id]
    print(f"🗑️ Product with ID {product_id} deleted successfully!")

def list_products():
    if not inventory:
        print("🚫 Inventory is empty.")
        return
    print("\n📋 Current Inventory:")
    print("-" * 60)
    print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Qty':<10} {'Logic':<10}")
    print("-" * 60)
    for product in inventory:
        print(f"{product['id']:<5} {product['name']:<20} ${product['price']:<9.2f} {product['quantity']:<10} {product['logic']:<10}")
    print("-" * 60)

def save_inventory():
    with open("inventory_data.txt", "w") as file:
        for product in inventory:
            line = f"{product['id']}|{product['name']}|{product['price']}|{product['quantity']}|{product['logic']}\n"
            file.write(line)

def load_inventory():
    global inventory
    inventory = []
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
        print("⚠️ No previous inventory file found.")

def evaluate_logic(expression):
    p1 = True
    p2 = False
    if "∧" in expression:
        return p1 and p2
    elif "∨" in expression:
        return p1 or p2
    elif "¬p1" in expression:
        return not p1
    elif "¬p2" in expression:
        return not p2
    elif "→" in expression:
        return (not p1) or p2
    elif "↔" in expression:
        return p1 == p2
    else:
        return False

def sort_inventory_by_logic():
    global inventory
    inventory.sort(key=lambda p: (p['price'], evaluate_logic(p['logic'])))
