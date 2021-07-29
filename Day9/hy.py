from database import Dabatase

class Product:
    def __init__(self, id, name, price):
        self.__id = id 
        self.name = name
        self.price = price

    def set_id (self, id):
        self.__id = id

    def get_id (self):
        return self.__id 
    def get_name(self):
        return self.name
    def show(self):
        print(f"Product: {self.__id} {self.name} {self.price}")

class Shop:
    def __init__(self, name, list_products):
        self.name = name
        self.list_products = list_products       
        
    def show(self):
        for item in self.list_products:
            print(f"Product Name: {item['product']} Amount: {item['amount']} Sold:{item['amount_sold']}")
            item["products"].show()

if __name__ == "__main__":
    db = Dabatase()
    
    list_product_objects = []

    for product in db.list_products:
        obj = Product(product['id'], product['name'], product['price'])
        list_product_objects.append({
            "amount": obj.get_id(),
            "product": obj.get_name(),
            "products": obj,
            "amount_sold":0
        })

    abc = Shop("Shop", list_product_objects)
    abc.show()


    