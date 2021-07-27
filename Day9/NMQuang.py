from database import Dabatase
import random


class Product():
    def __init__(self, id, name, price):

        # if type(price) != 'float' or type(id) != 'int':
        #     print('Wrong format!')

        self.__id = id
        self.__name = str(name)
        self.__price = price

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.price = price

    def show_info(self):
        return(self.__id, self.__name, self.__price)


class Shop():
    def __init__(self, name, list_products):
        self.name = name
        self.list_products = list_products


def main():
    db = Dabatase()
    list_products_object = []
    for product in db.list_products:
        obj = Product(product['id'], product['name'], product['price'])
        list_products_object.append({
            'amount': random.randint(10, 100),
            'product': obj,
            'amount_sold': random.randint(0, 10)
            })

    for product in list_products_object:
        product['product'].set_id(product['product'].get_id() + 1000)
        print(product['product'].show_info())


if __name__ == "__main__":
    main()
