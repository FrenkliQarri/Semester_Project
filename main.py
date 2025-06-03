from inventory_system import add_product, delete_product, list_products, save_inventory, load_inventory

def menu():
    print("Inventory Management System")
    print("1. Add Product")
    print("2. Delete Product")
    print("3. List Products")
    print("4. Save Inventory")
    print("5. Exit")

def main():
    load_inventory()

    while True:
        menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            try:
                product_id = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                price = float(input("Enter Product Price: "))
                quantity = int(input("Enter Product Quantity: "))
                logic = input("Enter Product Logic (e.g., p1 ∧ p2): ")
                add_product(product_id, name, price, quantity, logic)
            except ValueError:
                print("⚠️ Invalid input. Please try again.")
        elif choice == "2":
            try:
                product_id = int(input("Enter Product ID to delete: "))
                delete_product(product_id)
            except ValueError:
                print("⚠️ Invalid input. Please try again.")
        elif choice == "3":
            list_products()
        elif choice == "4":
            save_inventory()
        elif choice == "5":
            print("👋 Exiting the inventory system.")
            break
        else:
            print("⚠️ Invalid choice, please choose a valid option.")

if __name__ == "__main__":
    main()
