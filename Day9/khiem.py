from database import Dabatase
class Product :
    def __init__(self, id, name, price):
        if type(id) == int and type(name) == str and type(price) == float:
            self.__id = id
            self.name = name
            self.price = price
        else:
            print('Data Error ')

    # get id of product
    def get_id(self):
        return self.__id

    # set id of product   
    def set_id(self, id):
        self.__id = id

    def show(self):
        # for product in self.db_database:
        #     print(product)
        return(self.__id, self.name, self.price)

class Shop:
    def __init__(self, name_shop, list_products):
        self.name_shop = name_shop
        self.list_products = list_products

    def show(self):
        for item in self.list_products:
            print('----------------')
            print(f"Amount: {item['amount']}, Sold: {item['amount_sold']}")
            item['product'].show()
if __name__ == '__main__':
    db = Dabatase()
    db_database = []
    for products in db.list_products:
        obj = Product(products['id'], products['name'], products['price'])
        db_database.append({
            'amount': 25,
            'product': obj,
            'amount_sold': 0
        })
    # for product in db_database:
    #     print(product['product'].show_shop())
    #     # print(product.__id)
    shoppe = Shop('The thao', db_database)
    shoppe.show()