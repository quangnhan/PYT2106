from pathlib import Path


class Json:
    def __init__(self, path):
        self.json_file = open(path, 'w+')

    def show(self):
        print(self.json_file.read())

    def write(self, table):
        for row in table:
            self.json_file.write(f'{("----".join(row))}\n')

def main():
    path = Path.cwd() / 'Day11' / 'data' / 'data.csv'
    file = Json(path)
    file.show()

if __name__ == "__main__":
    main()
