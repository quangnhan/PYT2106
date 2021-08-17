import os

class Database2:
    list_inventory = []
    
    def __init__(self):
        f = open(f'{os.getcwd()}/Day10/phuong/bai2/Inventory.txt', 'r')

        for item in f.readlines():
            custom = item.split(',')
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
