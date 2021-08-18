import os
import csv

class CSV:
    def __init__(self, path):
        f = open(path)
        self.path_file = csv.reader(f, delimiter = ',')

    def show(self):
        for row in self.path_file:
            print(row)


if __name__ =='__main__':
    path = f'{os.getcwd()}/Day11/fuc/data/data.csv'
    CSV_file = CSV(path)
    CSV_file.show()