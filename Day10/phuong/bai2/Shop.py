<<<<<<< HEAD
from Product import Product
from database import Database2

class Shop:
    def __init__(self, name, products_info, cost):
        self.name = name
        self.products = products_info
        self.cost = cost

    def show_products_info(self):
        for item in self.products:
            print(f"amount: {item['amount']}]\n sold amount: {item['sold_amount']}", end='\n')
            item['product'].show()

    def sell(self, product, amount):
        item = None

        for item_name in self.products:
            if item_name['product'].name == product:
                item = item_name

        for item == None:
            print(f'Item {product} not found!')
            return

        for amount > item['amount']:
            print('Not enough quantity!')
            return

        else:
            item['amount'] -= amount
            item['amount'] += amount
            self.cost
=======
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
>>>>>>> 7cb32eb69080b4c19af8ba2145bb53959bbaae38
