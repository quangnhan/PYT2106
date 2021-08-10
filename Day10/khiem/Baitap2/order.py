from shop import Shop
from product import Product
class Order(Shop, Product):
    list_customers_order = []
    def __init__(self,name_customer, name_shop, product, amount):
        if super().check_product(product) == True:
            self.name_customer = name_customer
            self.name_shop = name_shop
            self.product = product
            self.amount = amount


    #cus order name_customer, name_shop, product, amount
    def cus_oder(self):
        Order.list_customers_order.append({
            "Name custommer": self.name_customer,
            "Name Shop":self.name_shop,
            "Product":self.product,
            "Amount buy":self.amount
        })

    def show_order(self):
        for order in Order.list_customers_order:
            print(order)

if __name__ == "__main__":

    customer1 = Order('khiem', "Stuart",' Quan jean', 150)
    # customer2 = Order("Thuy", "Jimmy",' Ao khoan', 120)
    print(customer1.cus_oder())
    print(Order.list_customers_order)
