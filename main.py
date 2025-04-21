from inventory_system import (
    add_product,
    delete_product,
    list_products,
    save_inventory,
    load_inventory,
    sort_inventory_by_logic
)

def main():
    load_inventory()

    # Initial products
    add_product(1, "Laptop", 999.99, 10, "p1 ∧ p2")
    add_product(2, "Smartphone", 699.99, 15, "p1 ∨ p2")
    add_product(3, "Headphones", 99.99, 20, "¬p1")
    add_product(4, "Tablet", 499.99, 8, "p1 → p2")
    add_product(5, "Smartwatch", 199.99, 12, "p1 ↔ p2")

    list_products()

    add_product(6, "Wireless Mouse", 29.99, 30, "¬p2")
    add_product(7, "Keyboard", 49.99, 25, "p1 ∧ ¬p2")
    add_product(8, "Monitor", 199.99, 15, "p2 → p1")
    add_product(9, "Speaker", 79.99, 20, "p1 ∨ ¬p2")

    delete_product(3)

    sort_inventory_by_logic()

    list_products()
    save_inventory()

if __name__ == "__main__":
    main()
