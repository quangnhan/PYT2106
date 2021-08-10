import os

class Json:
    def __init__(self, path) :
        self.json_file = open(path, 'r')
        self.path = path

    def show(self):
        print(self.json_file.read())

if __name__ == "__main__":
    path = f'{os.getcwd()}/Day11/data/data.txt'
    json = Json(path)
    json.show()