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
        print(self.__id, self.__name, self.__price)


class Shop():
    def __init__(self, name, list_products):
        self.name = name
        self.list_products = list_products

    def get_info(self):
        return (self.name, self.list_products)

    def show(self):
        print(self.name)
        for item in self.list_products:
            print(f"---------------------\nAmount: {item['amount']}\nAmount sold: {item['amount_sold']}\nProduct: {item['product'].get_name()}")


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

    myShop = Shop('myShop', list_products_object)
    print(myShop.get_info())


if __name__ == "__main__":
    main()
