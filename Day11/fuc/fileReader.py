import os
from CSV import CSV
from Json import Json 
from Excel import Excel
from PDF import PDF

class File_reader:
    __style_file = {
            'txt':Json,
            'csv': CSV,
            'xls': Excel,
            'pdf': PDF
        }
    def __init__(self,path):
        _, style_file = path.split('.')
        self.style_file = style_file
        self.file = self.__style_file[style_file](path)

    def show(self):
        self.file.show()

    def write(self, table):
        if self.style_file in ['txt', 'xls']:
            self.file.write(table)
        else:
            print('no such file')

if __name__ == '__main__':
    path =f"{os.getcwd()}/Day11/data/data.txt"
    file = File_reader(path)
    table = [
        ["Id", "Name", "Age"],
        ["1", "Nhan", "26"],
        ["2", "Hoan", "29"],
        ["3", "Khiem", "14"],
        ["4", "Viet", "29"],
        ["5", "Tung", "29"],
        ["6", "Khiet", "29"],
        ]
    file.show()
    file.write(table)
    file.show()