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
class Shop:
    def __init__(self, name, list_products):
        self.name = name
        self.list_products = list_products
    def show(self):
        for product in self.list_products:
            print("Amount:{0} Name:{2} Amount_sold:{1}".format(product['amount'], product['amount_sold'], product['product'].name))



if __name__ == "__main__":
    db = Dabatase()
    
    list_product_objects = []

    for product in db.list_products:
        obj = Product(product['id'], product['name'], product['price'])
        list_product_objects.append({
            "product": obj,
            "amount": 10,
            "amount_sold":1
        })
    # print(list_products_object)
    # for product in list_product_objects:
    #     print(product.name)
    shop1 = Shop("Shop 1", list_product_objects)
    shop1.show()    
