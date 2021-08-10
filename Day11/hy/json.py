import os

class ReadFile:
    def __init__(self, path):
        self.read_file = open(path, 'r')

    def show(self):
        print(self.read_file.read())

if __name__ == "__main__":
    path = f'{os.getcwd()}/Day11/data/data.txt'
    json = ReadFile(path)
    json.show()