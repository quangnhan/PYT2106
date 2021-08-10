from pathlib import Path

class Json:
    def __init__(self, path):
        self.json_file = open(path, 'r')

    def show(self):
        print(self.json_file.read())

def main():
    cwd = Path(__file__).parent.resolve()
    file = Json(cwd / 'data' / 'data.txt')
    # f = open(cwd / "data" / "data.txt")
    # print(f.readline())
    file.show()

if __name__ == "__main__":
    main()
