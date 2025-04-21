from inventory_system import add_product, delete_product, list_products, save_inventory, load_inventory

def menu():
    while True:
        print("Inventory Management System")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. List Products")
        print("4. Save Inventory")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        print(f"You entered: {choice}")  # Debugging line to check input

        if choice == '1':
            add_product()
        elif choice == '2':
            delete_product()
        elif choice == '3':
            list_products()
        elif choice == '4':
            save_inventory()
        elif choice == '5':
            print("Exiting the system.")
            break  # Exit the loop
        else:
            print("⚠️ Invalid choice, please choose a valid option.")

if __name__ == "__main__":
    menu()
