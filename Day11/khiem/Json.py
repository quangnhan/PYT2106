import os

class Json:
    def __init__(self, path):
        self.json_path = open(path, 'r')

    def show(self):
        print(self.json_path.read())

if __name__ == '__main__':
    path = (f'{os.getcwd()}/Day11/data/data.txt')
    read = Json(path)
    read.show()
