from abc import ABC, abstractmethod
import time
from typing import List, Callable, Tuple
import random
import sys
from collections import Counter

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
        return cls(int(parts[0]), parts[1], float(parts[2]), int(parts[3]), parts[4]) if len(parts) == 5 else None

def load_inventory(filename="/Users/apple/Desktop/Semester_Project/inventory_data.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                if line.strip() and (product := Product.from_line(line)):
                    inventory.append(product)
        print("✅ Inventory loaded successfully!")
    except Exception as e:
        print(f"⚠️ Error loading inventory: {e}")

def save_inventory(filename="/Users/apple/Desktop/Semester_Project/inventory_data.txt"):
    try:
        if not inventory:
            print("⚠️ Inventory is empty. Save cancelled.")
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
        inventory.append(Product(id, name, price, quantity, logic))
        print(f"✅ Product '{name}' added successfully!")
        save_inventory()

def delete_product(id):
    global inventory
    inventory = [p for p in inventory if p.id != id]
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
    found = [p for p in inventory if keyword.lower() in p.name.lower()]
    if not found:
        print("❌ No matching products found.")
    else:
        for product in found:
            print(product)

def filter_by_logic(expression):
    """Filter products by logic expression."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return
    print(f"🔎 Filtering products with logic: {expression}")
    for product in inventory:
        if expression in product.logic:
            print(product)

def filter_by_price_range(min_price, max_price):
    """Filter products within a price range."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return
    print(f"💰 Products between ${min_price:.2f} and ${max_price:.2f}")
    filtered = [p for p in inventory if min_price <= p.price <= max_price]
    if filtered:
        for product in filtered:
            print(product)
    else:
        print("No products found in this price range.")

def filter_by_quantity(min_quantity):
    """Filter products with quantity greater than or equal to minimum."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return
    print(f"📦 Products with quantity >= {min_quantity}")
    filtered = [p for p in inventory if p.quantity >= min_quantity]
    if filtered:
        for product in filtered:
            print(product)
    else:
        print("No products found with this quantity threshold.")

def calculate_total_inventory_value():
    total = sum(product.price * product.quantity for product in inventory)
    print(f"💰 Total Inventory Value: ${total:.2f}")

def filter_by_logic_operator(operator):
    """Filter products by logic operator."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return
    print(f"🧠 Logic contains operator '{operator}'")
    for product in inventory:
        if operator in product.logic:
            print(product)

def list_top_n_expensive_products(n=5):
    """List the top N most expensive products."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return
    sorted_products = sorted(inventory, key=lambda p: p.price, reverse=True)
    print(f"🏆 Top {n} Most Expensive Products")
    for product in sorted_products[:n]:
        print(product)

def list_low_stock(threshold=10):
    """List products with quantity below threshold."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return
    print(f"⚠️ Products with quantity < {threshold}")
    low_stock = [p for p in inventory if p.quantity < threshold]
    if low_stock:
        for product in low_stock:
            print(product)
    else:
        print("No products are low in stock.")

def average_price():
    """Calculate and display the average price of products."""
    if not inventory:
        print("⚠️ Inventory is empty.")
        return
    avg = sum(p.price for p in inventory) / len(inventory)
    print(f"📊 Average Price: ${avg:.2f}")

def average_quantity():
    """Calculate and display the average quantity of products."""
    if not inventory:
        print("⚠️ Inventory is empty.")
        return
    avg = sum(p.quantity for p in inventory) / len(inventory)
    print(f"📦 Average Quantity: {avg:.1f} units")

def most_common_logic():
    """Display the most common logic expression used in products."""
    if not inventory:
        print("⚠️ Inventory is empty.")
        return
    logics = [p.logic for p in inventory]
    most_common = Counter(logics).most_common(1)
    if most_common:
        logic, count = most_common[0]
        print(f"🧠 Most Common Logic Expression: '{logic}' (used {count} times)")
    else:
        print("No logic expressions found.")

def product_summary():
    """Display a summary of product statistics."""
    print("\n📈 Inventory Summary:")
    print("-------------------------------")
    average_price()
    average_quantity()
    most_common_logic()
    calculate_total_inventory_value()

def update_product_price(product_id, new_price):
    """Update the price of a product."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return
    for product in inventory:
        if product.id == product_id:
            old_price = product.price
            product.price = new_price
            print(f"✅ Updated price for {product.name} from ${old_price:.2f} to ${new_price:.2f}")
            save_inventory()
            return True
    print(f"❌ Product with ID {product_id} not found.")
    return False

def get_product_categories():
    """Get a list of all unique product categories."""
    categories = set()
    for product in inventory:
        if hasattr(product, 'category'):
            categories.add(product.category)
    return sorted(list(categories))

def get_supplier_list():
    """Get a list of all unique suppliers."""
    suppliers = set()
    for product in inventory:
        if hasattr(product, 'supplier'):
            suppliers.add(product.supplier)
    return sorted(list(suppliers))

def get_category_summary():
    """Display summary of products by category."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return
    categories = {}
    for product in inventory:
        if hasattr(product, 'category'):
            cat = product.category
            if cat not in categories:
                categories[cat] = {'count': 0, 'value': 0}
            categories[cat]['count'] += 1
            categories[cat]['value'] += product.price * product.quantity
    
    print("\n📊 Category Summary:")
    print("-" * 50)
    print(f"{'Category':<20} {'Products':<10} {'Total Value':<15}")
    print("-" * 50)
    for cat, data in categories.items():
        print(f"{cat:<20} {data['count']:<10} ${data['value']:<14.2f}")
    print("-" * 50)

def get_supplier_summary():
    """Display summary of products by supplier."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return
    suppliers = {}
    for product in inventory:
        if hasattr(product, 'supplier'):
            supp = product.supplier
            if supp not in suppliers:
                suppliers[supp] = {'count': 0, 'value': 0}
            suppliers[supp]['count'] += 1
            suppliers[supp]['value'] += product.price * product.quantity
    
    print("\n🏢 Supplier Summary:")
    print("-" * 50)
    print(f"{'Supplier':<20} {'Products':<10} {'Total Value':<15}")
    print("-" * 50)
    for supp, data in suppliers.items():
        print(f"{supp:<20} {data['count']:<10} ${data['value']:<14.2f}")
    print("-" * 50)

def get_inventory_health():
    """Display inventory health metrics."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return
    
    total_products = len(inventory)
    low_stock = len([p for p in inventory if p.quantity < 10])
    out_of_stock = len([p for p in inventory if p.quantity == 0])
    total_value = sum(p.price * p.quantity for p in inventory)
    
    print("\n🏥 Inventory Health Report")
    print("-" * 40)
    print(f"Total Products: {total_products}")
    print(f"Low Stock Items: {low_stock}")
    print(f"Out of Stock Items: {out_of_stock}")
    print(f"Total Inventory Value: ${total_value:.2f}")
    
    if total_products > 0:
        health_score = ((total_products - low_stock - out_of_stock) / total_products) * 100
        print(f"\nHealth Score: {health_score:.1f}%")
        if health_score >= 80:
            print("Status: 🟢 Healthy")
        elif health_score >= 60:
            print("Status: 🟡 Moderate")
        else:
            print("Status: 🔴 Needs Attention")
    print("-" * 40)

def get_product_recommendations():
    """Generate product recommendations based on inventory levels."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return
    
    low_stock = [p for p in inventory if p.quantity < 10]
    high_value = sorted(inventory, key=lambda p: p.price * p.quantity, reverse=True)[:5]
    
    print("\n💡 Product Recommendations:")
    print("-" * 50)
    
    if low_stock:
        print("\n⚠️ Low Stock Products:")
        for product in low_stock:
            print(f"- {product.name}: {product.quantity} units remaining")
    
    print("\n💰 High-Value Products:")
    for product in high_value:
        print(f"- {product.name}: ${product.price * product.quantity:.2f} total value")
    print("-" * 50)

def get_inventory_trends():
    """Display inventory trends and patterns."""
    if not inventory:
        print("⚠️ No products in inventory.")
        return
    
    prices = [p.price for p in inventory]
    avg_price = sum(prices) / len(prices)
    price_ranges = {
        'Low': len([p for p in prices if p < avg_price * 0.5]),
        'Medium': len([p for p in prices if avg_price * 0.5 <= p <= avg_price * 1.5]),
        'High': len([p for p in prices if p > avg_price * 1.5])
    }
    
    print("\n📈 Inventory Trends:")
    print("-" * 40)
    print("Price Distribution:")
    for range_name, count in price_ranges.items():
        print(f"{range_name}: {count} products")
    print("-" * 40)

def get_inventory_report():
    """Generate a comprehensive inventory report."""
    print("\n📑 Comprehensive Inventory Report")
    print("=" * 50)
    get_inventory_health()
    get_category_summary()
    get_supplier_summary()
    get_product_recommendations()
    get_inventory_trends()
    print("=" * 50)

def bubble_sort(items: List, key: Callable = lambda x: x) -> List:
    """Bubble sort implementation with performance tracking."""
    if not items: return []
    try:
        start_time = time.time()
        items_copy = items.copy()
        n = len(items_copy)
        for i in range(n):
            for j in range(0, n - i - 1):
                if key(items_copy[j]) > key(items_copy[j + 1]):
                    items_copy[j], items_copy[j + 1] = items_copy[j + 1], items_copy[j]
        print(f"Bubble Sort Time: {(time.time() - start_time):.6f} seconds")
        return items_copy
    except Exception as e:
        print(f"❌ Error in bubble sort: {str(e)}")
        return items

def quick_sort(items: List, key: Callable = lambda x: x) -> List:
    """Quick sort implementation with performance tracking."""
    if not items: return []
    try:
        start_time = time.time()
        def _quick_sort(arr):
            if len(arr) <= 1: return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if key(x) < key(pivot)]
            middle = [x for x in arr if key(x) == key(pivot)]
            right = [x for x in arr if key(x) > key(pivot)]
            return _quick_sort(left) + middle + _quick_sort(right)
        result = _quick_sort(items.copy())
        print(f"Quick Sort Time: {(time.time() - start_time):.6f} seconds")
        return result
    except Exception as e:
        print(f"❌ Error in quick sort: {str(e)}")
        return items

def merge_sort(items: List, key: Callable = lambda x: x) -> List:
    """Merge sort implementation with performance tracking."""
    if not items:
        print("⚠️ Empty list provided for sorting")
        return []
    
    try:
        start_time = time.time()
        items_copy = items.copy()
        
        def _merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if key(left[i]) <= key(right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        def _merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = _merge_sort(arr[:mid])
            right = _merge_sort(arr[mid:])
            return _merge(left, right)
        
        result = _merge_sort(items_copy)
        end_time = time.time()
        print(f"Merge Sort Time: {(end_time - start_time):.6f} seconds")
        return result
    except Exception as e:
        print(f"❌ Error in merge sort: {str(e)}")
        return items

def evaluate_truth_table(expression: str, variables: dict) -> bool:
    """Evaluate a logical expression using a truth table approach."""
    if not expression or not variables: return False
    try:
        expr = expression
        for var, value in variables.items():
            expr = expr.replace(var, str(value))
        return eval(expr)
    except Exception as e:
        print(f"❌ Error evaluating expression: {str(e)}")
        return False

def generate_truth_table(expression: str, variables: List[str]) -> None:
    """Generate and display a truth table for a given logical expression."""
    if not expression or not variables: return
    try:
        print(f"\nTruth Table for: {expression}")
        print("-" * (len(expression) + 20))
        print("Variables | Result")
        print("-" * (len(expression) + 20))
        for i in range(2 ** len(variables)):
            binary = format(i, f'0{len(variables)}b')
            var_dict = {var: bool(int(bit)) for var, bit in zip(variables, binary)}
            print(f"{binary} | {evaluate_truth_table(expression, var_dict)}")
    except Exception as e:
        print(f"❌ Error generating truth table: {str(e)}")

def evaluate_truth_table_step_by_step(expression: str, variables: dict) -> Tuple[bool, List[str]]:
    """Evaluate a logical expression with step-by-step explanation."""
    if not expression or not variables:
        print("⚠️ Invalid expression or variables")
        return False, ["Invalid input"]
    
    try:
        steps = []
        expr = expression
        steps.append(f"Original expression: {expr}")
        
        for var, value in variables.items():
            expr = expr.replace(var, str(value))
            steps.append(f"After replacing {var} with {value}: {expr}")
        
        result = eval(expr)
        steps.append(f"Final result: {result}")
        return result, steps
    except Exception as e:
        steps = [f"Error in evaluation: {str(e)}"]
        return False, steps

def generate_truth_table_with_steps(expression: str, variables: List[str]) -> None:
    """Generate and display a truth table with step-by-step evaluation."""
    if not expression or not variables:
        print("⚠️ Invalid expression or variables")
        return
    
    try:
        print(f"\nTruth Table for: {expression}")
        print("-" * (len(expression) + 20))
        print("Variables | Result | Steps")
        print("-" * (len(expression) + 20))
        
        n = len(variables)
        for i in range(2 ** n):
            binary = format(i, f'0{n}b')
            var_dict = {var: bool(int(bit)) for var, bit in zip(variables, binary)}
            result, steps = evaluate_truth_table_step_by_step(expression, var_dict)
            print(f"{binary} | {result} | {steps[0]}")
    except Exception as e:
        print(f"❌ Error generating truth table with steps: {str(e)}")

def analyze_performance():
    """Comprehensive performance analysis of sorting and inventory operations."""
    try:
        print("\n📈 Performance Analysis Report")
        print("=" * 50)
        
        print("\n🔍 Sorting Performance:")
        sizes = [100, 1000, 10000]
        for size in sizes:
            print(f"\nTesting with {size} items:")
            test_data = [random.randint(1, 1000) for _ in range(size)]
            bubble_sort(test_data)
            quick_sort(test_data)
        
        print("\n📊 Inventory Operations:")
        if not inventory:
            print("⚠️ Inventory is empty. Some operations may not be meaningful.")
            return
        
        start_time = time.time()
        search_by_name("test")
        print(f"Search Operation Time: {(time.time() - start_time):.6f} seconds")
        
        start_time = time.time()
        quick_sort(inventory, key=lambda x: x.price)
        print(f"Sort Operation Time: {(time.time() - start_time):.6f} seconds")
        
        print("\n💾 Memory Usage:")
        inventory_size = sys.getsizeof(inventory)
        print(f"Total inventory memory: {inventory_size / 1024:.2f} KB")
        if inventory:
            print(f"Average product memory: {sys.getsizeof(inventory[0])} bytes")
    except Exception as e:
        print(f"❌ Error in performance analysis: {str(e)}")

def demonstrate_sorting():
    """Demonstrate sorting algorithms on inventory data."""
    if not inventory:
        print("⚠️ No products in inventory to sort.")
        return
    print("\n🔄 Sorting Demonstration")
    print("=" * 50)
    print("\nSorting by price using Bubble Sort:")
    for item in bubble_sort(inventory, key=lambda x: x.price)[:5]:
        print(item)
    print("\nSorting by quantity using Quick Sort:")
    for item in quick_sort(inventory, key=lambda x: x.quantity)[:5]:
        print(item)

def demonstrate_truth_tables():
    """Demonstrate truth table evaluation."""
    print("\n📋 Truth Table Demonstration")
    print("=" * 50)
    generate_truth_table("A and B", ["A", "B"])
    generate_truth_table("(A and B) or (not C)", ["A", "B", "C"])
