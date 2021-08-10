import os
import PyPDF2

class PDF:
    def __init__(self, path):
        pdf = open(path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdf)
        self.pageObj = pdfReader.getPage(0)
    def show(self):
        print(self.pageObj.extractText())

if __name__ == "__main__":
    path = f'{os.getcwd()}/Day11/data/data.pdf'
    pdf = PDF(path)
    pdf.show()