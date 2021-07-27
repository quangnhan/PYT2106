from database import Dabatase


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


def main():
    db = Dabatase()
    list_products_object = []
    for product in db.list_products:
        obj = Product(product['id'], product['name'], product['price'])
        list_products_object.append(obj)

    for product in list_products_object:
        print(product.get_name())


if __name__ == "__main__":
    main()
