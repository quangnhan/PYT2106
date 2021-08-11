import PyPDF2
import os
from PyPDF2 import PdfFileReader

class PDF:
    def __init__(self, path):
        self.reader = PyPDF2.PdfFileReader(path)

    def show(self):
        pdf_data = self.reader.getPage(0)
        print(pdf_data.extractText())

    def write(self):
        None

    def extract_information(pdf_path):
        with open(pdf_path, 'rb') as f:
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()

        txt = f"""
        Information about {pdf_path}: 

        Author: {information.author}
        Creator: {information.creator}
        Producer: {information.producer}
        Subject: {information.subject}
        Title: {information.title}
        Number of pages: {number_of_pages}
        """

        print(txt)
        return information

    if __name__ == '__main__':
        path = 'data.pdf'
        extract_information(path)

if __name__ == "__main__":
    path = f'{os.getcwd()}/Day11/data/data.pdf'
    excel = PDF(path)
    # excel.show()