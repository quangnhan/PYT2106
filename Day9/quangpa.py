class Product:
    def __init__(self, id, name, price):
        print(self)
        # if type(price) != float or type(name) != str:
        #     print("Nhap lai")
        #     return
        self.id = id
        self.name = name
        self.price = price



if __name__ == "__main__":
    p = Product(1,"Quan", 100)
    print(p.name)