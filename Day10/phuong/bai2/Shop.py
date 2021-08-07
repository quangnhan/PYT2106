from database import Database
from Product import Product
from pprint import pprint

class Shop:
    def __init__(self, id, name, size, colour, price, list_products):
        super().__init__(id, name, size, colour, price)
        self.list_products = list_products

    def show(self):
        for item in self.list_products:
            print("--------------\n")
            pprint(f"Amount: {item['amount']}, Sold: {item['sold_amount']}")
            item["product"].show()

class Order(Shop):
    def __init__(self, id, name, size, colour, price, order):
        super().__init__(id, name, size, colour, price)
        self.order = order

    def get_order(self):
        for 

if __name__ == "__main__":
    db = Database()
    list_products_object = []

    for product in db.list_products:
        obj = Product(product['id'], product['name'],product['size'], product['colour'], product['price'])