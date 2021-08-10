
class Product:
    # count = 0
    def __init__(self, id, name, size, colour, price):
        self.id = id
        self.name = name
        self.size = size
        self.colour = colour
        self.price = price

    def show(self):
        pprint(f"id: {self.id}\n name: {self.name}\n size: {self.size}\n colour: {self.colour}\n price: {self.price}")
