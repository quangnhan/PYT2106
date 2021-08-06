from products import Product
from database import Database

class Shop:
    def __init__(self, name, products, money):
        self.products = products
        self.name = name 
        self.money = money

    def show_all_product(self):
        for item in self.products:
            print(f"amount: {item['amount']}\t amount sold: {item['amount_sold']}", end='\t')
            item['product'].show()

    def sell(self, product, amount):
        item = None

        #tìm product trong list
        for item_name in self.products:
            if item_name['product'].name == product:
                item = item_name
        
        if item == None: #nếu không có product-> return
            print(f'No product such as {product}')
            return

        #nếu số lượng lớn hơn số lượng hiện có -> return
        if amount > item['amount']:
            print('Not enough quantity')
            return
        else:
            item['amount'] -= amount
            item['amount_sold'] += amount
            self.money += amount*item['product'].price
            print(f"Sold!! {item['product'].name} price: {item['product'].price}")
            print(f'thanh tien: {item["product"].price*amount}')
            return {'shop name': self.name, 'product': product, 'amount': amount, 'price': amount*item['product'].price}


# tạo ra một vài cái shop để order gọi
Db = Database()
list_product = []
list_shop = {}
count = 0
for item in Db.list_database:
    product =Product(item['id'], item['name'], int(item['price']))
    list_product.append({'amount':10, 'product':product, 'amount_sold': 0})
    list_shop.update({f'shop{count}':Shop(f'shop{count}', list_product, 0)})
    count +=1
print(list_shop)

if __name__ == '__main__':
    '''Db = Database()
    list_product = []
    list_shop = []
    count = 0
    for item in Db.list_database:
        product =Product(item['id'], item['name'], item['price'])
        list_product.append({'amount':10, 'product':product, 'amount_sold': 0})
        list_shop.append({f'shop{count}':Shop(f'shop{count}', list_product, 0)})
        count +=1
    print(list_shop)'''
    pass