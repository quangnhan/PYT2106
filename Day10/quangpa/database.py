import os
import csv
import pprint
class database:
    product =[]
    def __init__(self):
        with open(f'{os.getcwd()}\Day10\quangpa\product.csv','rt')as f:
            data = csv.DictReader(f)
            self.product = [row for row in data]
            # print(product)
            # pprint.pprint(product,sort_dicts=False)
if __name__ == '__main__':
    db = database()
    print(db.product) 
    # # for i in range(0, len(db.product)):
    #     if db.product[i]['Name'] == 'Qu?n jean':
    #         # print(db.product[i])
    #         print(db.product[i])
    # db.Write_file()