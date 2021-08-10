import os
from Json import Json
from CSV import CSV
from Excel import Excel
from PDF import PDF

class FileReader:
    __file_class = {
        'txt': Json,
        'csv': CSV,
        'xls': Excel,
        'pdf': PDF
    }

    def __init__(self, p):
        name, file_type = p.split('.')
        print("DEBUG file_type", file_type)
        self.file_reader = self.__file_class[file_type](p)

    def show(self):
        self.file_reader.show()

if __name__ == "__main__":
    # p = f'{os.getcwd()}/Day11/data/data.txt'
    # p = f'{os.getcwd()}/Day11/data/data.csv'
    # p = f'{os.getcwd()}/Day11/data/data.xls'
    p = f'{os.getcwd()}/Day11/data/data.pdf'
    file_reader = FileReader(p)
    file_reader.show()
