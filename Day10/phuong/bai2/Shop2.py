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

    def trading_mechanism(self, product, amount):
        item = None

        #serach in list the item
        for item_name in self.products:
            if item_name['product'].name == product:
                item = item_name

        #if the item not in list
        if item == None:
            print(f'{product} not found!')
        return

        #if the inventory quantity doesn't reach order quantity 
        if amount > item['amount']:
            print("not enough quantity!")