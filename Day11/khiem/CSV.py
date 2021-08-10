import os
import csv

class CSV:
    def __init__(self,path):
        f = open(path)
        self.csv = csv.reader(f, delimiter=',')
        self.path = path

    def show(self):
        for row in self.csv:
            print(row)

if __name__ == "__main__":
    path = f'{os.getcwd()}/Day11/data/data.csv'
    cfile = CSV(path)
    cfile.show()