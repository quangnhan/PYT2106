from pathlib import Path
from Json import Json
from CSV import CSV
# from PDF import PDF
from Excel import Excel


class FileReader:
    __file_class = {
            '.txt': Json,
            '.csv': CSV,
            # '.pdf': PDF,
            '.xls': Excel
            } 

    def __init__(self, path):
        self.file_reader = self.__file_class[path.suffix](path)

    def show(self):
        self.file_reader.show()


def main():
    # path = Path.cwd() / 'Day11' / 'data' / 'data.txt'
    # path = Path.cwd() / 'Day11' / 'data' / 'data.csv'
    # path = Path.cwd() / 'Day11' / 'data' / 'data.pdf'
    path = Path.cwd() / 'Day11' / 'data' / 'data.xls'
    file_reader = FileReader(path)
    file_reader.show()

if __name__ == "__main__":
    main()
