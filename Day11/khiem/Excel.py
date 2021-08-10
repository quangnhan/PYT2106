import os
import pandas as pd

class Excel:
    def __init__(self, path):
        self.excel = pd.read_excel(path)

    def show(self):
        df = pd.DataFrame(self.excel, columns=['Name'])
        for row in df['Name']:
            print(row)

if __name__ == '__main__':
    path = f'{os.getcwd()}/Day11/data/data.xls'
    excel = Excel(path)
    excel.show()