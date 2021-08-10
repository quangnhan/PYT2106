import os

class Json:
    def __init__(self, path):
        path = f'{os.getcwd()}/data/file.txt'
        self.json_file = open(path, 'r')

    def show(self):
        print(self.json_file.read())

if __name__ == "__main__":
    path = f'{os.getcwd()}/bai11_20210810/data/file.txt'
    json = Json(path)
    json.show()