from inventory_system import add_product, delete_product, list_products, save_inventory, load_inventory

def menu():
    """Display the menu and handle user input."""
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. List Products")
        print("4. Save Inventory")
        print("5. Exit")
        
        try:
            choice = int(input("Choose an option (1-5): "))
            
            if choice == 1:
                try:
                    id = int(input("Enter product ID: "))
                    name = input("Enter product name: ")
                    price = float(input("Enter product price: $"))
                    quantity = int(input("Enter product quantity: "))
                    logic = input("Enter product logic (e.g., p1 ∧ p2): ")
                    add_product(id, name, price, quantity, logic)
                except ValueError:
                    print("⚠️ Invalid input. Please enter correct data types.")
            
            elif choice == 2:
                try:
                    id = int(input("Enter product ID to delete: "))
                    delete_product(id)
                except ValueError:
                    print("⚠️ Invalid input. Please enter a valid product ID.")
            
            elif choice == 3:
                list_products()
            
            elif choice == 4:
                save_inventory()
            
            elif choice == 5:
                print("Goodbye!")
                break
            
            else:
                print("⚠️ Invalid choice, please choose a valid option.")
        
        except ValueError:
            print("⚠️ Invalid input. Please choose a number between 1 and 5.")

def main():
    load_inventory()
    menu()

if __name__ == "__main__":
    main()
