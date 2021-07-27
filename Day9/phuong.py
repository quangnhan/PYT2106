class Product:
    def __init__(self, id, name, price):
        self._id = id
        self.name = str(name)
        self.price = price

        if type(id) != 'int' or type(price)!= 'float':
            print('Error')
            return

if __name__ == "__main__":
    quan = Product(1,"Quan jean", 100)
    ao = Product(2, "Ao thun", 150)

print(quan)