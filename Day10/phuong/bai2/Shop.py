from database import Database2
from Product import Product

class Shop:
    def __init__(self, name, products, cost):
        self.name = name
        self.products = products
        self.cost = cost

    def show_all_products(self):
        for item in self.products:
            print("--------------\n")
            print(f"Amount: {item['amount']}, Sold: {item['sold_amount']}")
            item["product"].show()

if __name__ == "__name__":
    db = Database2

    list_products_object = []

    for product in db.list_products:
        obj = Product(product['id'], product['name'], product['price'])
        list_products_object.append({
            "amount": 10,
            "product" : obj,
            "sold_amount" : 1
        })

    xxx_shop = Shop("Xxx Shop", list_products_object)
    xxx_shop.show_all_products()