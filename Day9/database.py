import os 

class Dabatase:
    list_products = []

    def __init__(self):
        f = open(f'{os.getcwd()}/Day9/products.txt', 'r')

        for line in f.readlines():
            id, name, price = line.split(',')
            self.list_products.append({
                'id' : int(id),
                'name' : name,
                'price' : float(price.replace('\n',"")),
            })

if __name__ == "__main__":
    db = Dabatase()
    print(db.list_products)