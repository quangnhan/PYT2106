import os

class Database2:
    list_products = []

    def __init__(self):
        f = open(f'{os.getcwd()}/Day10/phuong/bai2/Inventory.txt', 'r')

        for line in f.readline():
            id, name, size, colour, price = line.split(',')
            self.list_products.append({
                'id' : int(id),
                'name' : name,
                'size' : size,
                'colour': colour,
                'price' : float(price.replace('\n', "")),
            })
            return line

if __name__ == "__main__":
    db = Database2()
    print(db.list_products)