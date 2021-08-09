from database import*

class Product:
    list_of_products = []
    def __init__(self, id, name, size, colour, price):
        self.id = id
        self.name = name
        self.size: str(size)
        self.colour = colour
        self.price = price

    def show(self):
        print(f'id: {self.id}\n name: {self.name}\n size: {self.size}\n colour: {self.colour}\n price: {self.price}\n')
