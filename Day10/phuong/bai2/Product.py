<<<<<<< HEAD
from database import*
=======
from database import Database
from pprint import pprint

>>>>>>> 7cb32eb69080b4c19af8ba2145bb53959bbaae38

class Product:
    list_of_products = []
    def __init__(self, id, name, size, colour, price):
        self.id = id
        self.name = name
        self.size: str(size)
        self.colour = colour
        self.price = price

<<<<<<< HEAD
    def show(self):
        print(f'id: {self.id}\n name: {self.name}\n size: {self.size}\n colour: {self.colour}\n price: {self.price}\n')
=======
if __name__ == "__main__":
    db = Database
    list_products_object = []
    for product in db.list_products:
        list_products_object.append({
            'amount' : 69,
            'product': Product(product['id'], product['name'], product['size'],product['colour'],product['price']),
            'amount_sold': 0
        })
>>>>>>> 7cb32eb69080b4c19af8ba2145bb53959bbaae38
