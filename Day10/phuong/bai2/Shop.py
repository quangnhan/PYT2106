from Product import Product
from database import Database2

class Shop:
    def __init__(self, name, products, cost):
        self.name = name
        self.products = products
        self.cost = cost

    def show_all_prod(self):
        for item in self.products:
            print(f"amount: {item['inventory_amount']}\n sold")
