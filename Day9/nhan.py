class Product:
    def __init__(self, id, name, price):
        self.id = id 
        self.name = name
        self.price = price


if __name__ == "__main__":
    quan = Product(1, "Quan jean", 100)
    ao = Product(2, "ao thun", 150)
    
    print(quan)
