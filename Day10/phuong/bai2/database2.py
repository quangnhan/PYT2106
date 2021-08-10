<<<<<<< HEAD:Day10/phuong/bai2/database2.py
=======
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

>>>>>>> 803213afcf97a6230bb679ab6c0d4502b0950dd3:Day10/phuong/bai2/database.py
import os

class Database2:
    list_inventory = []
    
    def __init__(self):
        f = open(f'{os.getcwd()}/Day10/phuong/bai2/Inventory.txt', 'r')
<<<<<<< HEAD:Day10/phuong/bai2/database2.py

        for item in f.readlines():
            item_contribution = item.split(',')
=======
        for line in f.readlines():
            custom = line.split(',')
>>>>>>> 803213afcf97a6230bb679ab6c0d4502b0950dd3:Day10/phuong/bai2/database.py
            self.list_inventory.append({
                'id': custom[0],
                'name': custom[1],
                'size': custom[2],
                'colour': custom[3],
                'price': custom[4]
            })

if __name__ == "__main__":
    db = Database2()
<<<<<<< HEAD:Day10/phuong/bai2/database2.py
    print(db.list_inventory)
=======
    print(db.list_inventory)
>>>>>>> 803213afcf97a6230bb679ab6c0d4502b0950dd3:Day10/phuong/bai2/database.py
