from database import Dabatase
class Product :
    def __init__(self, id, name, price):
        if type(id) == int and type(name) == str and type(price) == float:
            self.__id = id
            self.name = name
            self.price = price
        else:
            print('Data Error ')

    # get id of product
    def get_id(self):
        return self.__id

    # set id of product   
    def set_id(self, id):
        self.__id = id


if __name__ == '__main__':
    db = Dabatase()
    db_database = []
    for products in db.list_products:
        p = Product(products['id'], products['name'], products['price'])
        db_database.append(p)

    for product in db_database:
        print(product.get_id())
        # print(product.__id)