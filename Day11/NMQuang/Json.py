from pathlib import Path


class Json:
    def __init__(self, path):
        self.json_file = open(path, 'r')

    def show(self):
        print(self.json_file.read())


def main():
    path = Path.cwd() / 'Day11' / 'data' / 'data.csv'
    file = Json(path)
    file.show()

if __name__ == "__main__":
    main()
