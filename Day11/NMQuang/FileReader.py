from pathlib import Path
from Json import Json
from CSV import CSV
from PDF import PDF
from Excel import Excel


class FileReader:
    __file_class = {
            '.txt': Json,
            '.csv': CSV,
            '.pdf': PDF,
            '.xls': Excel
            } 

    def __init__(self, path):
        self.file_reader = self.__file_class[path.suffix](path)
        self.path = path

    def show(self):
        self.file_reader.show()

    def write(self, table):
        if self.path.suffix in ['.txt', '.xls']:
            self.file_reader.write(table)
        else:
            print("Write method not found for this file type.")

def main():
    # path = Path.cwd() / 'Day11' / 'data' / 'data.txt'
    # path = Path.cwd() / 'Day11' / 'data' / 'data.csv'
    # path = Path.cwd() / 'Day11' / 'data' / 'data.pdf'
    path = Path.cwd() / 'Day11' / 'NMQuang' / 'data' / 'data.xls'
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
    file_reader.show()
    file_reader.write(table)

if __name__ == "__main__":
    main()
