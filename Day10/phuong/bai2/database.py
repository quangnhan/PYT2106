from Day10.phuong.bai2.Product import Product
import os

class Database2:
    list_inventory = []

#     def __init__(self):
#         f = open(f'{os.getcwd()}/Day10/phuong/bai2/Inventory.txt', 'r')

#         for line in f.readline():
#             id, name, size, colour, price = line.split(',')
#             self.list_products.append({
#                 'id' : int(id),
#                 'name' : name,
#                 'size' : size,
#                 'colour': colour,
#                 'price' : float(price.replace('\n', "")),
#             })
#             return line

# if __name__ == "__main__":
#     db = Database2()
#     print(db.list_products)

    def __init__(self):
        f = open(f'{os.getcwd()}\Day10\\phuong\\bai2\\Inventory.txt', 'r')

        for item in f.readline():
            item_contribution = item.split(',')
            self.list_inventory.append({
                'id' : item_contribution[0],
                'name' : item_contribution[1],
                'size' : item_contribution[2],
                'colour' : item_contribution[3],
                'price' : item_contribution[4],
            })

if __name__ == "__main__":
    db = Database2
