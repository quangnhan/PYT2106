from database import Dabatase

class Product:
    def __init__(self, id, name, price):
        self.id = id 
        self.name = name
        self.price = price

if __name__ == "__main__":
    db = Dabatase()
    
    list_product_objects = []

    for product in db.list_products:
        obj = Product(product['id'], product['name'], product['price'])
        list_product_objects.append(obj)

    for product in list_product_objects:
        print(product.name)

    
