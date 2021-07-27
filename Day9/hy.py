class Product:
    def __init__(self, id, name, price):
        if type(id) != int or type(name) != str or type(price) != float:
            print("Error")
            return
        self.id = id
        self.name = name
        self.price = price

    def show(self):
        print("ID la "+ str(self.id))

if __name__ == "__main__":
    p = Product(1, "Hy",100.00)
    print(p.name)
    print(p.price)
    p.show()