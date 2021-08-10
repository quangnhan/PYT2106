from Shop2 import Shop, list_shop

class Order:
    list_order = []
    def __init__(self, customer_name, shop_name, product, amount):
        self.customer_name = customer_name
        self.shop_name = shop_name
        self.product = product
        self.amount = amount

        if self.shop_name not in list_shop.key():
            print(f"Shop {self.shop_name} not found!")
            return
        else:
            self.sell = list_shop[shop_name].sell(product, amount)
            #double check the order
            Order.list_order.append({
                'customer name': customer_name,
                'order': self.sell
            })
        
    def show_all_order(self):
        for order in Order.list_order:
            print(order)

if __name__ == "__main__":
    print(list_shop)
    order1=Order('Mr.A', 'shop1', 'T-shirt', 1)
    order1=Order('Mr.A', 'shop1', 'Ao dai', 2)
    print(Order.list_order)
    print(list_shop['shop1'].money)