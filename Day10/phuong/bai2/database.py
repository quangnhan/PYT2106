from Day10.phuong.bai2.Product import Product
import os
# import pprint (note)

class Database2:
    list_inventory = []
<<<<<<< HEAD
#bao loi "ValueError: not enough values to unpack (expected 5, got 1)". chua xu ly duoc
    # def __init__(self):
    #     f = open(f'{os.getcwd()}\\Day10\phuong\\bai2\\Inventory.txt', 'r')
=======

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
>>>>>>> 7cb32eb69080b4c19af8ba2145bb53959bbaae38

    #     for line in f.readline():
    #         id, name, size, colour, price = line.split(',')
    #         self.list_inventory.append({
    #             'id' : int(id),
    #             'name' : name,
    #             'size' : size,
    #             'colour': colour,
    #             'price' : float(price.replace('\n', "")),
    #         })
    #         return line
#da tham khao cua fuc de viet lai, thank you!
    def __init__(self):
<<<<<<< HEAD
        for item in open(f'{os.getcwd()}\Day10\\phuong\\bai2\\Inventory.txt').read().split('\n'):
            inventory_item = item.split(',')
            self.list_inventory.append({'id': inventory_item[0], 'name': inventory_item[1], 'size': inventory_item[2], 'colour': inventory_item[3], 'price': inventory_item[4]})

if __name__ == "__main__":
    db = Database2()
    print(db.list_inventory)
=======
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
>>>>>>> 7cb32eb69080b4c19af8ba2145bb53959bbaae38
