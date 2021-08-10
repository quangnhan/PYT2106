import PyPDF2
import os

class PDF:
    def __init__(self, path):
        self.reader = PyPDF2.PdfFileReader(path)

    def show(self):
        pdf_data = self.reader.getPage(0)
        print(pdf_data.extractText())

if __name__ == "__main__":
    path = f'{os.getcwd()}/Day11/data/data.pdf'
    excel = PDF(path)
    excel.show()