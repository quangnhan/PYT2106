from pathlib import Path
import pandas as pd


class Excel:
    def __init__(self, path):
        self.excel = pd.read_excel(path)

    def show(self):
        df = pd.DataFrame(self.excel, columns=['Name'])
        for data in df['Name']:
            print(data)

                
def main():
    path = Path.cwd() / 'Day11' / 'data' / 'data.xls'
    file = Excel(path)
    file.show()

if __name__ == "__main__":
    main()
