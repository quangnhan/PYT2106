import os
import PyPDF2

class PDF:
    def __init__(self, path):
        self.pdf = open(path, 'rb')
    def show(self):
        print(self.pdf.read())
if __name__ == "__main__":
    path = f'{os.getcwd()}/Day11/data/data.pdf'
    pdf = PDF(path)
    pdf.show()