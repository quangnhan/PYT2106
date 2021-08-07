import random
from database import Database
from pprint import pprint


class Product:
    # count = 0
    def __init__(self, id, name, size, colour, price):
        self._id = id
        self._name = name
        self.size = size
        self.colour = colour
        self._price = price

    def get_id(self):
        return self._id

    def set_id(self, new_id):
        self._id = new_id

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def set_price(self, new_price):
        self._price = new_price

    def get_info(self):
        print(f'ID = {self._id}, Name = {self._name}, Size = {self.size}, Colour = {self.colour}, Price = {self._price}')

if __name__ == "__main__":
    db = Database
    list_products_object = []
    for product in db.list_products:
        list_products_object.append({
            'amount' : random.randint(1, 100),
            'product': Product(product['id'], product['name'], product['size'],product['colour'],product['price']),
            'amount_sold': random.randint(0,100)
        })