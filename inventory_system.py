from abc import ABC, abstractmethod

inventory = []

class ItemBase(ABC):
    def __init__(self, id, name, price, quantity, logic):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.logic = logic

    @abstractmethod
    def to_line(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Product(ItemBase):
    def to_line(self):
        return f"{self.id}|{self.name}|{self.price}|{self.quantity}|{self.logic}"

    def __str__(self):
        return f"{self.id:<5} {self.name:20} ${self.price:8.2f}   {self.quantity:3}     {self.logic}"

    @classmethod
    def from_line(cls, line):
        parts = line.strip().split('|')
        if len(parts) == 5:
            return cls(int(parts[0]), parts[1], float(parts[2]), int(parts[3]), parts[4])
        else:
            raise ValueError("Invalid data format")

def load_inventory(filename=None):
    if filename is None:
        filename = "/Users/apple/Desktop/Semester_Project/inventory_data.txt"
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
        filename = "/Users/apple/Desktop/Semester_Project/inventory_data.txt"
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
    if any(product.id == id for product in inventory):
        print(f"⚠️ Product with ID {id} already exists.")
    else:
        new_product = Product(id, name, price, quantity, logic)
        inventory.append(new_product)
        print(f"✅ Product '{name}' added successfully!")
        save_inventory()

def delete_product(id):
    global inventory
    inventory = [product for product in inventory if product.id != id]
    print(f"🗑️ Product with ID {id} deleted successfully!")
    save_inventory()

def list_products():
    if not inventory:
        print("⚠️ No products in inventory.")
        return

    print(f"🧪 Inventory contains: {len(inventory)} products")
    print("📋 Current Inventory:")
    print("------------------------------------------------------------")
    print("ID    Name                 Price      Qty        Logic")
    print("------------------------------------------------------------")
    for product in inventory:
        print(product)
    print("------------------------------------------------------------")

def search_by_name(keyword):
    print(f"🔍 Searching for '{keyword}'...")
    found = [p for p in inventory if keyword.lower() in p.name.lower()]
    if not found:
        print("❌ No matching products found.")
    else:
        for product in found:
            print(product)

def filter_by_logic(expression):
    print(f"🔎 Filtering products with logic: {expression}")
    filtered = [p for p in inventory if expression in p.logic]
    for product in filtered:
        print(product)

def filter_by_price_range(min_price, max_price):
    print(f"💲 Products between ${min_price:.2f} and ${max_price:.2f}")
    for product in inventory:
        if min_price <= product.price <= max_price:
            print(product)

def filter_by_quantity(min_qty):
    print(f"📦 Products with quantity ≥ {min_qty}")
    for product in inventory:
        if product.quantity >= min_qty:
            print(product)

def calculate_total_inventory_value():
    total = sum(product.price * product.quantity for product in inventory)
    print(f"💰 Total Inventory Value: ${total:.2f}")

def filter_by_logic_operator(operator):
    print(f"🧠 Logic contains operator '{operator}'")
    for product in inventory:
        if operator in product.logic:
            print(product)

def list_top_n_expensive_products(n=5):
    sorted_products = sorted(inventory, key=lambda p: p.price, reverse=True)
    print(f"🏆 Top {n} Most Expensive Products")
    for product in sorted_products[:n]:
        print(product)

def list_low_stock(threshold=10):
    print(f"⚠️ Products with stock less than {threshold}")
    for product in inventory:
        if product.quantity < threshold:
            print(product)

def average_price():
    if not inventory:
        print("⚠️ Inventory is empty.")
        return
    avg = sum(p.price for p in inventory) / len(inventory)
    print(f"📊 Average Product Price: ${avg:.2f}")

def list_all_logic_expressions():
    logics = sorted(set(p.logic for p in inventory))
    print("📚 Unique Logic Expressions in Inventory:")
    for logic in logics:
        print(f"- {logic}")

def product_summary():
    print("📝 Inventory Summary:")
    print(f"Total Products: {len(inventory)}")
    calculate_total_inventory_value()
    average_price()
    list_low_stock(5)
    list_top_n_expensive_products(3)
