from inventory_module import add_product, delete_product, list_products

def main():
    # Add initial products
    initial_products = [
        (1, "Laptop", 999.99, 10),
        (2, "Smartphone", 699.99, 15),
        (3, "Headphones", 99.99, 20),
        (4, "Tablet", 499.99, 8),
        (5, "Smartwatch", 199.99, 12)
    ]
    
    # Add initial products to inventory
    for product in initial_products:
        add_product(*product)
    
    # Display initial inventory
    list_products()
    
    # Example of adding a new product
    add_product(6, "Wireless Mouse", 29.99, 30)
    add_product(7, "Keyboard", 49.99, 25)
    add_product(8, "Monitor", 199.99, 15)
    add_product(9, "Speaker", 79.99, 20) 
    # Display inventory after adding new product
    list_products()
    
    # Example of deleting a product
    delete_product(3)  # Delete Headphones
    
    # Display final inventory
    list_products()

if __name__ == "__main__":
    main() 