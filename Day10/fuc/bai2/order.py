from shop import Shop, list_shop



class Order:
    list_order = []
    def __init__(self, name_customer, shop_name, product, amount):
        self.name_customer = name_customer
        self.product = product
        self.amount = amount
        self.shop_name = shop_name
        # tìm xem shop_name nó có nằm trong list_shop hay không
        if self.shop_name not in list_shop.keys():
            print(f'no shop name such ass {self.shop_name}')
            return
        else:
            self.sell = list_shop[shop_name].sell(product, amount)
            # tạo một cái list các order để check
            Order.list_order.append({'name customer':name_customer, 'order':self.sell})

    def show_all_order(self):
        for order in Order.list_order:
            print(order)

if __name__ =="__main__":
    print(list_shop)
    o1=Order('fucdeeptry', 'shop1', 'Quan jean', 3)
    o2=Order('fucdeeptry', 'shop1', 'Quan jean', 3)
    print(Order.list_order)
    print(list_shop['shop1'].money)
    
