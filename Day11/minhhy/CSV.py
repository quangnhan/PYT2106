import os
import csv

class CSV:
    def __init__(self, path):
        f = open(path)
        self.csv = csv.reader(f, delimiter=',')

    def show(self):
        for row in self.csv:
            print(row)

if __name__ == "__main__":
    path = f'{os.getcwd()}/Day11/data/file.csv'
    csv_file = CSV(path)
    csv_file.show()