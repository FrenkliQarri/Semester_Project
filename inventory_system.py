import os

inventory = []

class Product:
    def __init__(self, id, name, price, quantity, logic):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.logic = logic

    def to_line(self):
        return f"{self.id}|{self.name}|{self.price}|{self.quantity}|{self.logic}"

    @staticmethod
    def from_line(line):
        parts = line.strip().split('|')
        if len(parts) != 5:
            raise ValueError("Invalid data format")
        return Product(int(parts[0]), parts[1], float(parts[2]), int(parts[3]), parts[4])

    def __str__(self):
        return f"{self.id:<5} {self.name:<20} ${self.price:8.2f}   {self.quantity:<3}     {self.logic}"

def load_inventory(filename=None):
    if filename is None:
        filename = os.path.join(os.path.dirname(__file__), "inventory_data.txt")
    try:
        with open(filename, "r") as file:
            for line in file:
                if line.strip() == "":
                    continue
                product = Product.from_line(line)
                inventory.append(product)
        print("✅ Inventory loaded successfully!")
    except FileNotFoundError:
        print("⚠️ Inventory file not found, starting with an empty inventory.")
    except Exception as e:
        print(f"⚠️ Error loading inventory: {e}")

def save_inventory(filename=None):
    if filename is None:
        filename = os.path.join(os.path.dirname(__file__), "inventory_data.txt")
    try:
        if not inventory:
            print("⚠️ Inventory is empty. Save cancelled to avoid overwriting.")
            return
        with open(filename, "w") as file:
            for product in inventory:
                file.write(product.to_line() + "\n")
        print("✅ Inventory saved successfully!")
    except Exception as e:
        print(f"⚠️ Error saving inventory: {e}")

def add_product(id, name, price, quantity, logic):
    if any(p.id == id for p in inventory):
        print(f"⚠️ Product with ID {id} already exists.")
    else:
        try:
            new_product = Product(id, name, price, quantity, logic)
            inventory.append(new_product)
            print(f"✅ Product '{name}' added successfully!")
            save_inventory()
        except Exception as e:
            print(f"⚠️ Error adding product: {e}")

def delete_product(id):
    global inventory
    before = len(inventory)
    inventory = [p for p in inventory if p.id != id]
    after = len(inventory)
    if before == after:
        print(f"⚠️ No product with ID {id} found.")
    else:
        print(f"🗑️ Product with ID {id} deleted successfully!")
        save_inventory()

def list_products():
    print("🧪 Inventory contains:", len(inventory), "products")
    if not inventory:
        print("⚠️ No products in inventory.")
        return

    print("📋 Current Inventory:")
    print("------------------------------------------------------------")
    print("ID    Name                 Price      Qty        Logic")
    print("------------------------------------------------------------")
    for product in inventory:
        print(product)
    print("------------------------------------------------------------")
