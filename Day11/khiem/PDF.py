import os
import PyPDF2

class PDF:
    def __init__(self, path):
        self.reader = PyPDF2.PdfFileReader(path)

    def show(self):
        pdf_data = self.reader.getPage(0)
        print(pdf_data)

if __name__ == '__main__':
    path = f'{os.getcwd()}/Day11/data/data.pdf'
    pdf = PDF(path)
    pdf.show()