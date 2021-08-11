import PyPDF2
from pathlib import Path


class PDF:
    def __init__(self, path):
        self.reader = PyPDF2.PdfFileReader(path)

    def show(self):
        pdf_data = self.reader.getPage(0)
        print(pdf_data.extractText())


def main():
    path = Path.cwd() / 'Day11' / 'data' / 'data.pdf'
    file = PDF(path)
    file.show()

if __name__ == "__main__":
    main()

