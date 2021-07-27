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

#    def set_name(self):
#        self.price = price


def main():
    db = Dabatase()
    list_products_object = []
    for product in db.list_products:
        obj = Product(product['id'], product['name'], product['price'])
        list_products_object.append(obj)

    for product in list_products_object:
        print(product.get_info())

if __name__ == "__main__":
    main()