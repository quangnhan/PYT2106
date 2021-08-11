from pathlib import Path
import pandas as pd


class Excel:
    def __init__(self, path):
        self.path = path

    def show(self):
        self.excel = pd.read_excel(self.path)
        df = pd.DataFrame(self.excel, columns=['Name'])
        for data in df['Name']:
            print(data)
 
    def write(self, table):
        dataframe = dict()
        for i in range(len(table[0])):
            dataframe[table[0][i]] = [x[i] for x in table[1:]]
        df = pd.DataFrame(dataframe)
        df = df[table[0]]
        writer = pd.ExcelWriter(self.path, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)
        # workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        (max_row, max_col) = df.shape
        column_settings = [{'header': column} for column in df.columns]
        worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})
        worksheet.set_column(0, max_col - 1, 12)
        writer.save()
        
                
def main():
    path = Path.cwd() / 'Day11' / 'NMQuang' / 'data' / 'data.xls'
    table = [
        ["Name", "Age"],
        ["Nhan", "26"],
        ["Hoan", "29"],
        ["Khiem", "14"],
        ["Viet", "29"],
        ]
    file = Excel(path)
    file.write(table)

if __name__ == "__main__":
    main()
