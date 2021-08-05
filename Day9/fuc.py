from database import Dabatase
import os

#class Product
class Product:
    count=0
    def __init__(self, id , name, price):
        if type(id) != int or type(name) != str or type(price) != float:
            print('Error')
            return

        Product.count +=1
        self.__id = id
        self.name=name
        self.price = price
    
    def show(self):
        print(self.__id, self.name, self.price, sep='\t')

    def getId(self):
        print(self.__id)

    def getName(self):
        print(self.name)

    def getPrice(self):
        print(self.price)

    def setId(self, newId):
        self.__id =newId


#class shop
class Shop:
        
    def __init__(self, name, list_product, money):
        self.name= name
        self.list_products = list_product
        self.__money = money

    def show(self):
        for item in self.list_products:
            print('_________________________________')
            print(f'amount: {item["amount"]},\t amount sold: {item["amount_sold"]}')
            item['product'].show()

    def __showProduct(self, product):
        for item in self.list_products:
            if item['product'].name == product:
                productobj = item
        print(f'amount: {productobj["amount"]},\t amount sold: {productobj["amount_sold"]}')
        productobj['product'].show()

    def show_Money(self):
        print('money:',self.__money)

    #sell some product
    def sell(self, product, amount=1):
        print('\n\n')
        productobj = False
        for item in self.list_products:
            if item['product'].name == product:
                productobj = item
        
        if productobj == False:
            print(f'no product such as \'{product}\'')
            return
        
        if productobj['amount'] ==0:
            print('Out of stock!!!')
            return

        print(f'sold!!! name:{productobj["product"].name}, price: {productobj["product"].price}')
        self.__money += productobj["product"].price*amount
        productobj['amount'] -= amount
        productobj['amount_sold'] += amount
        self.__showProduct(product)
        self.show_Money()


    

if __name__ == '__main__':
    '''
    p1=Product(1, 'p1', 6.5)
    print(p1.id)
    print(p1.count)
    p2=Product(2,'p2', 5.5)
    print(Product.count)
    Product.showName(p2)
    '''
    
    db = Dabatase().list_products
    '''
    list_products = []
    for product in db:
        item = Product(product['id'], product['name'], product['price'])
        list_products.append(item)
    '''

    list_product_object = []

    for product in db:
        item = Product(product['id'], product['name'], product['price'])
        list_product_object.append({'amount': 10, 'product': item, 'amount_sold':0})
    
    #check
    '''
    for item in list_product_object:
        print(item['product'].name)
    '''

    shop1 = Shop('abc', list_product_object, 0)
    shop1.show()
    shop1.sell('Quan the thao')