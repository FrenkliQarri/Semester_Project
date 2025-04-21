inventory = []

def add_product(product_id, name, price, quantity, in_stock):
    product = {
        'id': int(product_id),
        'name': str(name),
        'price': float(price),
        'quantity': int(quantity),
        'in_stock': bool(in_stock)
    }
    inventory.append(product)

def save_inventory(filename="inventory_data.txt"):
    with open(filename, "w") as file:
        for p in inventory:
            line = f"{p['id']}|{p['name']}|{p['price']}|{p['quantity']}|{p['in_stock']}\n"
            file.write(line)

def load_inventory(filename="inventory_data.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                id_, name, price, qty, stock = line.strip().split("|")
                add_product(id_, name, price, qty, stock == 'True')
    except FileNotFoundError:
        pass

def list_products():
    if not inventory:
        print("Inventory is empty.")
        return
    print(f"{'ID':<5} {'Name':<15} {'Price':<8} {'Qty':<5} {'In Stock'}")
    for p in inventory:
        print(f"{p['id']:<5} {p['name']:<15} {p['price']:<8} {p['quantity']:<5} {p['in_stock']}")
