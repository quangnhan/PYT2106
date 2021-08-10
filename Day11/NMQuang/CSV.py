from pathlib import Path
import csv


class CSV:
    def __init__(self, path):
        f = open(path)
        self.csv = csv.reader(f, delimiter=',')

    def show(self):
        for row in self.csv:
            print(row)


def main():
    path = Path.cwd() / 'Day11' / 'data' / 'data.csv'
    file = CSV(path)
    file.show()

if __name__ == "__main__":
    main()

