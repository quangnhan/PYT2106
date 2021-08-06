class Product:
    def __init__(self, id, name, price):
        self.name= name
        self.id = id
        self.price = price

    def show(self):
        print(f'id: {self.id}\t name: {self.name} \t price:{self.price}')