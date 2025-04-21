# main.py
from inventory_system import add_product, delete_product, list_products, save_inventory, load_inventory

def main():
    """Main function to simulate the inventory system."""
    # Example adding products
    add_product(1, "Laptop", 999.99, 10, "p1 ∧ p2")
    add_product(2, "Smartphone", 699.99, 15, "p1 ∨ p2")
    add_product(3, "Headphones", 99.99, 20, "¬p1")
    add_product(4, "Tablet", 499.99, 8, "p1 → p2")
    add_product(5, "Smartwatch", 199.99, 12, "p1 ↔ p2")
    
    # List products to check if duplicates were prevented
    print("\n📋 Current Inventory:")
    list_products()

    # Save the inventory to a file
    save_inventory()

if __name__ == "__main__":
    main()
