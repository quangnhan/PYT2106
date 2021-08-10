import os
import pandas as pd
from xlsxwriter import Workbook

class Excel:
    def __init__(self, path):
        self.excel = pd.read_excel(path)

    def show(self):
        df = pd.DataFrame(self.excel, columns=['Name'])
        for row in df['Name']:
            print(row)
    
    def write(self, table):
        # Create a Pandas dataframe from some data.
        # df = pd.DataFrame({
        #     'Country':    ['China',    'India',    'United States', 'Indonesia'],
        #     'Population': [1404338840, 1366938189, 330267887,       269603400],
        #     'Rank':       [1,          2,          3,               4]})
        # df = pd.DataFrame({
        #     'Name': table [0],
        #     'Age': table[1]
        #     })
        dataFrame = dict()
        for i in range(len(table[0])):
            dataFrame[table[0][i]] = [x[i] for x in table[1:]]

        df = pd.DataFrame(dataFrame)
        # Order the columns if necessary.
        # df = df[['Rank', 'Country', 'Population']]
        df = df[table[0]]
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter('pandas_table.xlsx', engine='xlsxwriter')

        # Write the dataframe data to XlsxWriter. Turn off the default header and
        # index and skip one row to allow us to insert a user defined header.
        df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)

        # Get the xlsxwriter workbook and worksheet objects.
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        # Get the dimensions of the dataframe.
        (max_row, max_col) = df.shape

        # Create a list of column headers, to use in add_table().
        column_settings = [{'header': column} for column in df.columns]

        # Add the Excel table structure. Pandas will add the data.
        worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})

        # Make the columns wider for clarity.
        worksheet.set_column(0, max_col - 1, 12)

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

if __name__ == '__main__':
    path = f'{os.getcwd()}/Day11/khiem/data.xls'
    excel = Excel(path)
    table = [
        ["Name", "Age"],
        ["Nhan", "26"],
        ["Hoan", "29"],
        ["Khiem", "14"],
        ["Viet", "29"],
        ]
    # excel.show()
    excel.write(table)