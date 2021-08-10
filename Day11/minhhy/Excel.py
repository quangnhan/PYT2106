import os
import pandas as pd



class Excel:
    def __init__(self, path):
        self.excel = pd.read_excel(path)


    def show(self):
        df = pd.DataFrame(self.excel, columns=['Name'])
        for i in df['Name']:
            print(i)

if __name__ == "__main__":
    path = f'{os.getcwd()}/Day11/data/data.xls'
    excel = Excel(path)
    excel.show()