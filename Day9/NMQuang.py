from database import Dabatase


class Product():
    def __init__(self, id, name, price):

        # if type(price) != 'float' or type(id) != 'int':
        #     print('Wrong format!')

        self.__id = id
        self.name = str(name)
        self.price = price

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id = id

#     def set_name(self, name):
#         self.name = name
# 
#     def set_price(self, price):
#         self.price = price


def main():
    db = Dabatase()
    list_products_object = []
    for product in db.list_products:
        obj = Product(product['id'], product['name'], product['price'])
        list_products_object.append(obj)

    for product in list_products_object:
        print(product.name)


if __name__ == "__main__":
    main()
