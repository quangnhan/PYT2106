class Product:
    def __init__(self, id, name_product, amount, price):
        if type(id) == int and type(name_product) == str and type(price) ==float:           
            self.__id = id
            self.__name_product = name_product
            self.__amount = amount
            self.__price = price
        else:
            print("Data is Error: Invalid")

    def set_id(self, id):
        self.__id = id

    def get_id(self, id):
        return self.__id
    
    def set_price(self, price):
        self.__price = price

    def get_price(self, price):
        return self.__price

    def get_amount(self, amount):
        return self.__amount

    def set_name(self, name_product):
        self.__name_product = name_product

    def get_name(self, name_product):
        return self.__name_product

    def show(self):
        print(f'Product: id:{self.__id} Name:{self.__name_product} Amount:{self.__amount} Price:{self.__price}')

if __name__ == "__main__":
    ao = Product(1,"AO",200 , 500.0)
    ao.show()