from product import Product
from database import Database
from random import randint
#add product from database into list list_products
db = Database()
list_products = []
for product in db.list_products:
    product = Product(product['id'], product['name'], product['amount'], product['price'])
    list_products.append({
        'product': product,
        'amount_sold': 0
    })
class Shop():
    def __init__(self, name_shop, list_products):
        self.name_shop = name_shop
        self.list_products = list_products
    items = None
    def sell_product(self, name, amount):
       
        #search item in list_products
        for item_name in db.list_products:
            if item_name['name'] == name:
                items = item_name
                items['amount'] -= amount
                print(f"Product: {items['name']}\t Price: {items['price']}\t Amount: {amount}")
             
        if items ==None:
            print(f'Product {name} is not found ')
    
    def check_product(self, name):
         for item_name in db.list_products:
                if item_name['name'] == name:
                    return True
                
        
      
    def show(self):
        for item in self.list_products:
            item['product'].show()
            print(f"Sold: {item['amount_sold']}")
            print('-----------------')

if __name__ == "__main__":
    NBK = Shop("Stuart", list_products)
    NBK.sell_product('Ao khoan',2)
    NBK.sell_product('Quan jean',50)
