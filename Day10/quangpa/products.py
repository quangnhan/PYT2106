from database import database
import pprint
class Product:
    def __init__(self, id, name, Price, Quantity, Shop):
        self.__id = id
        self.__name = name
        self.__Price = Price
        self.__Quantity = Quantity
        self.__Shop = Shop
    def show(self):
        print('Product: ID: {0} Name:{1} Price:{2} Quantity:{3} Shop:{4}'.format(self.__id, self.__name, self.__Price, self.__Quantity, self.__Shop))


class Shop:
    def __init__(self,name, list_products):
        self.__name = name
        self.list_products = list_products
    def show(self):
        print('Sản phẩm có ở SHOP {0}: '.format(self.__name))
        for item in self.list_products:
            print('Product: ID: {0} Name:{1} Price:{2} Quantity:{3}'.format(item['ID'], item['Name'], item['Price'], item['Quantity']))


class Order:
    def __init__(self,list_oder):
        self.list_oder = list_oder
    def check_out(self):
        for item in self.list_oder:
            print("Hoa don phai tra la: {}".format(sum(item['Total']))),
if __name__ == '__main__':
    db = database()
    # Hiển thị toàn bộ sản phẩm
    for product in db.product:
        obj = Product(product['ID'], product['Name'], product['Price'], product['Quantity'],product['Shop'])
        print(obj.show())


    #Hiển thị sản phẩm theo cửa hàng
    Name_shop = input("Please input name shop: ")
    list_products_obj=[]
    for i in range(0, len(db.product)):
        if db.product[i]['Shop'] == Name_shop:
            list_products_obj.append(db.product[i])   
    shop = Shop(Name_shop,list_products_obj)
    shop.show()


    #Thanh toán sản phẩm
    list_order = []
    Name_Order = input("Nhap san pham muon mua: ")
    Shop_Order = input("Nhap cua hang muon chuyen hang:")
    Quantity_Order = int(input("Nhap so luong ban muon mua:"))
    for i in range(0,len(db.product)):
        if db.product[i]['Shop'] == Shop_Order and db.product[i]['Name'] == Name_Order:
            if int(db.product[i]['Quantity']) >= Quantity_Order:
                list_order.append({
                        'Name': Name_Order,
                        "Total": db.product[i]['Price']*Quantity_Order,
                        "Shop": db.product[i]['Shop']
                    })
            else:
                print("Ton kho khong du")
    order = Order(list_order)
    print(order.check_out())
    