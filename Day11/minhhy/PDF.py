import os
import PyPDF2

class PDF:
    def __init__(self, path):
        self.pdf = PyPDF2.PdfFileReader(path)

    def show(self):
        pdf_data = self.pdf.getPage(0)
        print(pdf_data.extractText())

if __name__ == "__main__":
    path = f'{os.getcwd()}/Day11/data/data.pdf'
    pdf = PDF(path)
    pdf.show()