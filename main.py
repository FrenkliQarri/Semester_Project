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
    load_inventory
)

def main():
    load_inventory()

    add_product(1, "Laptop", 999.99, 10, "p1 and p2")
    add_product(2, "Phone", 699.50, 5, "not p1")
    add_product(3, "Mouse", 25.75, 100, "p2 or not p1")
    
    list_products()
    search_by_name("Phone")
    filter_by_logic("p1")
    filter_by_price_range(20, 1000)
    filter_by_quantity(10)
    calculate_total_inventory_value()
    filter_by_logic_operator("and")
    list_top_n_expensive_products()
    list_low_stock(10)
    average_price()
    average_quantity()
    most_common_logic()
    product_summary()

if __name__ == "__main__":
    main()
