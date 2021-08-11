import os
from Json import Json
from CSV import CSV
from PDF import PDF
from Excel import Excel

class FileReader:
    __file_class = {
        'txt' : Json,
        'csv' : CSV,
        'pdf' : PDF,
        'xls' : Excel,
    }
    
    def __init__(self, path):
        _, self.file_type = path.split('.')
        self.file_reader = self.__file_class[self.file_type](path)

    def show(self):
        self.file_reader.show()

    def write(self, table):
        if self.file_type in ['txt', 'xls']:
            self.file_reader.write(table)
        else:
            print("You not implement write method")

if __name__ == "__main__":
    # path = f'{os.getcwd()}/Day11/nhan/data/data.txt'
    # path = f'{os.getcwd()}/Day11/data/data.csv'
    # path = f'{os.getcwd()}/Day11/data/data.pdf'
    path = f'{os.getcwd()}/Day11/nhan/data/data.xls'

    table = [
        ["Id", "Name", "Age"],
        ["1", "Nhan", "26"],
        ["2", "Hoan", "29"],
        ["3", "Khiem", "14"],
        ["4", "Viet", "29"],
        ["5", "Tung", "29"],
        ["6", "Khiet", "29"],
        ]
    file_reader = FileReader(path)
    file_reader.write(table)