from inventory_system import add_product, delete_product, list_products, save_inventory, load_inventory

def main():
    # Add initial products
    initial_products = [
        (1, "Laptop", 999.99, 10, "p1 ∧ p2"),
        (2, "Smartphone", 699.99, 15, "p1 ∨ p2"),
        (3, "Headphones", 99.99, 20, "¬p1"),
        (4, "Tablet", 499.99, 8, "p1 → p2"),
        (5, "Smartwatch", 199.99, 12, "p1 ↔ p2")
    ]
    
    # Add initial products to inventory
    for product in initial_products:
        add_product(*product)
    
    # Display initial inventory
    list_products()
    
    # Example of adding a new product
    add_product(6, "Wireless Mouse", 29.99, 30, "¬p2")
    add_product(7, "Keyboard", 49.99, 25, "p1 ∧ ¬p2")
    add_product(8, "Monitor", 199.99, 15, "p2 → p1")
    add_product(9, "Speaker", 79.99, 20, "p1 ∨ ¬p2") 
    
    # Display inventory after adding new products
    list_products()
    
    # Example of deleting a product
    delete_product(3)  # Delete Headphones
    
    # Display final inventory
    list_products()

    # Save and load functionality
    save_inventory()  # Save to file
    load_inventory()  # Load from file
    
    # Display loaded inventory
    list_products()

if __name__ == "__main__":
    main()
