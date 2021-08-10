import os
from CSV import CSV
from Json import Json

class FileReader:
    __file_class = {
        'txt' : Json,
        'csv' : CSV,
    }

    def __init__(self, path):
        _, file_type = path.split('.')
        self.file_reader = self.__file_class[file_type](path)

    def show(self):
        self.file_reader.show()

if __name__ == "__main__":
    # path = f'{os.getcwd()}/Day11/data/data.txt'
    path = f'{os.getcwd()}/Day11/data/data.csv'

    file_reaeder = FileReader(path)
    file_reaeder.show()