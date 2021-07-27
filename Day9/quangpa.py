from database import Dabatase
class Product:
    def __init__(self, id, name, price):
        self.__id = id
        self.name = name
        self.price = price
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id

if __name__ == "__main__":
    # db = Dabatase()
    
    # list_product_objects = []

    # for product in db.list_products:
    #     obj = Product(product['id'], product['name'], product['price'])
    #     list_product_objects.append(obj)

    # for product in list_product_objects:
    #     print(product.name)
    quan = Product(1,"quan", 100)
    quan.id = 2
    quan.set_id(2)
    print(quan.get_id())

