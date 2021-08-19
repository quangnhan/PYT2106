import os

class Json:
    def __init__(self, path):
        self.path = path
    
    def show(self):
        self.f = open(self.path, 'r')
        print(self.f.read())
        self.f.close()

    def write(self, table):
        self.f = open(self.path, 'w+')
        for row in table:
            self.f.write(f"{('    ').join(row)}\n")
        self.f.close()


if __name__ =='__main__':
    path = f"{os.getcwd()}/Day11/data/data.txt"
    json = Json(path)
    table = [
        ["Id", "Name", "Age"],
        ["1", "Nhan", "26"],
        ["2", "Hoan", "29"],
        ["3", "Khiem", "14"],
        ["4", "Viet", "29"],
        ["5", "Tung", "29"],
        ["6", "Khiet", "29"],
        ]
    json.write(table)
    json.show()