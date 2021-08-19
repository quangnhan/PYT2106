import os
import pandas as pd


class Excel:
    def __init__(self, path):
        self.path = path
        

    def show(self):
        self.excel = pd.read_excel(path,index_col=0, header=0)
        print(self.excel)
        

    def write(self, table):
        df = pd.DataFrame({
            a:[A[table[0].index(a)] for A in table[1:]] for a in table[0]
        })

        # Order the columns if necessary.
        df = df[['Id', 'Name', 'Age']]

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(self.path, engine='xlsxwriter')

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

if __name__ == "__main__":
    path = f'{os.getcwd()}/Day11/fuc/data/data.xls'
    excel = Excel(path)
    table = [
        ["Id", "Name", "Age"],
        ["1", "Nhan", "26"],
        ["2", "Hoan", "29"],
        ["3", "Khiem", "14"],
        ["4", "Viet", "29"],
        ["5", "Tung", "29"],
        ["6", "Khiet", "29"],
        ]
    excel.write(table)
    excel.show()