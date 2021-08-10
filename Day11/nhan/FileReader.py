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
        _, file_type = path.split('.')
        self.file_reader = self.__file_class[file_type](path)

    def show(self):
        self.file_reader.show()

if __name__ == "__main__":
    # path = f'{os.getcwd()}/Day11/data/data.txt'
    # path = f'{os.getcwd()}/Day11/data/data.csv'
    # path = f'{os.getcwd()}/Day11/data/data.pdf'
    path = f'{os.getcwd()}/Day11/data/data.xls'

    file_reader = FileReader(path)
    file_reader.show()