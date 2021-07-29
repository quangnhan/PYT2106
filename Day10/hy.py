from animal import Animal

class Cat(Animal):
    def __init__(self,name,weight,height, gioitinh, soChan):
        super().__init__(name, weight,height)
        self._gioitinh = gioitinh
        self._soChan = soChan


    def show(self):
        print(f"Cat : {self._name}, gioi tinh : {self._gioitinh}, So chi: {self._soChan}")

    def get_gioitinh(self):
        return self._gioitinh
    def get_soChan(self):
        return self._soChan
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def set_gioitinh(self, gioitinh):
        self._gioitinh = gioitinh


    def set_soChan(self, soChan):
        self._soChan = soChan    
if __name__ == "__main__":
    cat = Cat("Lucky", 100, 45, 'male', 4)
    cat.set_name(" Tom")
    cat.show()