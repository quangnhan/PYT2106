from database import Dabatase
from pprint import pprint

class Product:
    def __init__(self, id, name, price):
        self.__id = id 
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_name(self, name):
        self.__name = name

    def show(self):
        print(f"Product: {self.__id} {self.__name} {self.__price}")

class Shop:
    def __init__(self, name, list_products):
        self.name = name
        self.list_products = list_products

    def show(self):
        for item in self.list_products:
            print("----------------")
            print(f"Amount: {item['amount']} Sold: {item['amount_sold']}")
            item["product"].show()

if __name__ == "__main__":
    db = Dabatase()
    
    list_product_objects = []

    for product in db.list_products:
        obj = Product(product['id'], product['name'], product['price'])
        list_product_objects.append({
            "amount": 10,
            "product": obj,
            "amount_sold":0,
        })

    nhan_shop = Shop("Nhan Shop", list_product_objects)
    nhan_shop.show()


 


    
