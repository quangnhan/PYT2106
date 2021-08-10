from database2 import Database2
from Product2 import Product

class Shop:
    def __init__(self, sname, products, cost):
        self.sname = sname
        self.products = products
        self.cost = cost

    def show_all_products(self):
        for item in self.products:
            print("--------------\n")
            print(f"Amount: {item['amount']}, Sold: {item['sold_amount']}")
            item["product"].show()

    def sell(self, product, amount):
        item = None

        #serach in list the item
        for item_name in self.products:
            if item_name['product'].name == product:
                item = item_name

        #if the item not in list
        if item == None:
            print(f'{product} not found!')
        return

        #if the quantity is bigger than the inventory
        if amount > product['amount']:
            print("Quantity is not enough!")
            return
        else:
            item['amount'] -= amount
            item['sold_amount'] += amount
            self.cost += amount*item['product'].price
            print(f"Item have been sold {item['product'].name} Cost: {item['product'].cost}")
            print(f"Thanh tien: {item['Product'].price*amount}")
            return {'Shop name': self.sname, 'product': product, 'amount': amount, 'cost': amount*item['product'].cost}

db = Database2()
list_products = []
list_shop = {}
count = 0
for item in db.list_inventory:
    product = Product(item['id'], item['name'], item['size'], item['colour'], item['price'])
    list_products.append({
        'amount': 10,
        'product': product,
        'sold_amount': 1
    })
    list_shop.update({f'shop{count}':Shop(f'shop{count}', list_products,0)})
    count +=1
print(list_shop)