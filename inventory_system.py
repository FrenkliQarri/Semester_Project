from abc import ABC, abstractmethod
import itertools

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

def evaluate_logic_expression(expression, p1, p2):
    try:
        expr = expression.replace("¬", "not ").replace("∧", " and ").replace("∨", " or ")
        expr = expr.replace("→", " or not ").replace("↔", " == ")
        return eval(expr, {}, {"p1": p1, "p2": p2})
    except:
        return False

def generate_truth_table(expression):
    table = []
    for p1, p2 in itertools.product([True, False], repeat=2):
        result = evaluate_logic_expression(expression, p1, p2)
        table.append((p1, p2, result))
    return table

def display_all_truth_tables():
    if not inventory:
        print("⚠️ No products in inventory.")
        return

    print("\n📊 Logic Truth Tables for All Products")
    print("======================================")
    for product in inventory:
        print(f"🧩 Product: {product.name} (ID: {product.id})")
        print(f"Logic: {product.logic}")
        print("p1      p2      Result")
        print("------------------------")
        table = generate_truth_table(product.logic)
        for p1, p2, result in table:
            print(f"{str(p1):<8}{str(p2):<8}{str(result)}")
        print("------------------------\n")
