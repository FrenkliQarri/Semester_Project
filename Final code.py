class Product:
    def __init__(self, product_id, name, price, quantity, condition_expr):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.condition_expr = condition_expr  # logical expression string

class InventorySystem:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
    
    def delete_product(self, product_id):
        self.products = [p for p in self.products if p.id != product_id] 