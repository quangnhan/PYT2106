class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        if type(price) != float:
            print("Nhap lai")
        elif type(name) != str:
            print("Nhập lại")
        else:
            continue
