from _typeshed import Self
from os import name
from database import Dabatase

class Product():

    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self):
        self.__name = name

    def get__price(self):
        return self.__price

    def get_info(self):
        print(f'Id = {self.__id}, Name = {self.__name}, Price = {self.__price}')

#   def set_price(self):
#        self.__price = 
class Shop():
    def __init__(self, name, list_products):
        self.__name = name
        self.__list_products = list_products

    def get_info(self):
        return(self.name, self.list_products)

    def show(self):
        print(self.name)
        for item in self.list_products:
            print('------------\n')
            print(f"Amount: {item['amount']}, Product:{item['product'].get_name()} , Sold: {item['sold_amount']}")

if __name__ == "__main__":
    db = Dabatase()
    list_products_object = []

    for product in db.list_products:
        obj = Product(product['id'], product['name'], product['price'])
        list_products_object.append({
            "amount": 14,
            "product": obj,
            "sold_amount": 0
        })

    ceeShop = Shop('ceeShop', list_products_object)
    ceeShop.show()