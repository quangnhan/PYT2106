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