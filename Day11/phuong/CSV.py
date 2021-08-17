import os
import csv

class CSV:
    def __init__(self, path):
        f = open(path)
        self.csv = csv.reader(path, delimiter= ',')

    def show(self):
        for row in self.csv:
            print(row)

    def write(write):
        for 

if __name__ == "__main__":
    path = f'{os.getcwd()}/Day11/data/data.csv'
    csv_file = CSV(path)
    csv_file.show()

