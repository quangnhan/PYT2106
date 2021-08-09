# import pprint (note)

#bao loi "ValueError: not enough values to unpack (expected 5, got 1)". chua xu ly duoc
    # def __init__(self):
    #     f = open(f'{os.getcwd()}\\Day10\phuong\\bai2\\Inventory.txt', 'r')
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

import os

class Database2:
    list_inventory = []
    
    def __init__(self):
        f = open(f'{os.getcwd()}/Day10/phuong/bai2/Inventory.txt', 'r')
        for line in f.readlines():
            custom = line.split(',')
            self.list_inventory.append({
                'id': custom[0],
                'name': custom[1],
                'size': custom[2],
                'colour': custom[3],
                'price': custom[4]
            })

if __name__ == "__main__":
    db = Database2()
    print(db.list_inventory)