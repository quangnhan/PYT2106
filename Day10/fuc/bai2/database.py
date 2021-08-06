import os

class Database:
    list_database =[]
    def __init__(self):
        for item in open(f'{os.getcwd()}\Day10\\fuc\\bai2\\products.txt','r').read().split('\n'):
            product_item = item.split(',')
            self.list_database.append({'id': product_item[0], 'name': product_item[1], 'price': product_item[2]})


if __name__ == '__main__':
    db = Database()
    print(db.list_database)