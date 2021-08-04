from Day9.database import Dabatase
import os

class Database:
    list_products = []

    def __init__(self):
        f = open(f'{os.getcwd()}/Day10/phuong/bai2/List_DB.txt', 'r')

        for line in f.readline:
            id, name, size, colour, price = line.split(',')
            self.list_product.append({
                'id' : int(id),
                'name': str(name),
                'size': int(size),
                'colour': str(colour),
                'price': float(price.replace('\n', ""))
            })

if __name__ == "__main__":
    db = Dabatase
    print(db.list_products)