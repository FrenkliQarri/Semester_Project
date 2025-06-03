from inventory_system import (
    add_product,
    delete_product,
    list_products,
    search_by_name,
    filter_by_logic,
    filter_by_price_range,
    filter_by_quantity,
    calculate_total_inventory_value,
    filter_by_logic_operator,
    list_top_n_expensive_products,
    list_low_stock,
    average_price,
    average_quantity,
    most_common_logic,
    product_summary,
    update_product_price,
    load_inventory,
    save_inventory
)

def menu():
    print("\n📋 Inventory Management Menu")
    print("1. Add Product")
    print("2. Delete Product")
    print("3. List Products")
    print("4. Search by Name")
    print("5. Filter by Logic")
    print("6. Filter by Price Range")
    print("7. Filter by Quantity")
    print("8. Calculate Total Value")
    print("9. Filter by Logic Operator")
    print("10. List Top Expensive Products")
    print("11. List Low Stock")
    print("12. Show Average Price")
    print("13. Show Average Quantity")
    print("14. Show Most Common Logic")
    print("15. Show Product Summary")
    print("16. Update Product Price")
    print("0. Exit")

def get_valid_input(prompt, input_type=str):
    """Get valid input from user with error handling."""
    while True:
        try:
            value = input(prompt).strip()
            if input_type == int:
                return int(value)
            elif input_type == float:
                return float(value)
            return value
        except ValueError:
            print(f"❌ Invalid input. Please enter a valid {input_type.__name__}.")

def main():
    # Load inventory at startup
    load_inventory()
    
    while True:
        menu()
        choice = input("Choose an option (0-16): ").strip()

        if choice == "1":
            pid = get_valid_input("Enter Product ID: ", int)
            name = get_valid_input("Enter Product Name: ")
            price = get_valid_input("Enter Price: ", float)
            qty = get_valid_input("Enter Quantity: ", int)
            logic = get_valid_input("Enter Logic: ")
            add_product(pid, name, price, qty, logic)
        
        elif choice == "2":
            pid = get_valid_input("Enter Product ID to delete: ", int)
            delete_product(pid)

        elif choice == "3":
            list_products()

        elif choice == "4":
            keyword = get_valid_input("Enter product name to search: ")
            search_by_name(keyword)

        elif choice == "5":
            logic = get_valid_input("Enter logic expression to filter: ")
            filter_by_logic(logic)

        elif choice == "6":
            min_price = get_valid_input("Enter minimum price: ", float)
            max_price = get_valid_input("Enter maximum price: ", float)
            filter_by_price_range(min_price, max_price)

        elif choice == "7":
            min_qty = get_valid_input("Enter minimum quantity: ", int)
            filter_by_quantity(min_qty)

        elif choice == "8":
            calculate_total_inventory_value()

        elif choice == "9":
            operator = get_valid_input("Enter logic operator: ")
            filter_by_logic_operator(operator)

        elif choice == "10":
            n = get_valid_input("Enter number of products to show: ", int)
            list_top_n_expensive_products(n)

        elif choice == "11":
            threshold = get_valid_input("Enter low stock threshold: ", int)
            list_low_stock(threshold)

        elif choice == "12":
            average_price()

        elif choice == "13":
            average_quantity()

        elif choice == "14":
            most_common_logic()

        elif choice == "15":
            product_summary()

        elif choice == "16":
            pid = get_valid_input("Enter Product ID: ", int)
            new_price = get_valid_input("Enter new price: ", float)
            update_product_price(pid, new_price)

        elif choice == "0":
            # Save inventory before exiting
            save_inventory()
            print("👋 Exiting the Inventory System. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
