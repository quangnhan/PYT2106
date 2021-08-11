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
        'pdf': PDF,
    }
    def __init__(self,path):
        _,file_type = path.split('.')
        self.file_reader = self.__file_class[file_type](path)

    def show(self):
        self.file_reader.show()

    def write(self,table):
        self.file_reader.writer(table)
if __name__ == '__main__':
    #path = f'{os.getcwd()}\Day11\data\data.txt'
    # path = f'{os.getcwd()}\Day11\data\data.csv'
    path = f'{os.getcwd()}/Day11/data/data.xls'
    # path = f'{os.getcwd()}/Day11/data/data.pdf'
    table = [
        ['Name', 'Age'],
        ['A','20'],
        ['B','18'],
        ['C','21']
    ]
    file_reader = FileReader(path)
    file_reader.write(table)