from inventory_system import *

def main():
    load_inventory()
    add_product(1, "Laptop", 999.99, 10, True)
    add_product(2, "Phone", 499.99, 20, True)
    add_product(3, "Keyboard", 49.99, 30, True)
    list_products()
    save_inventory()

if __name__ == "__main__":
    main()
