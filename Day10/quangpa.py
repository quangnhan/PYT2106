from animal import Animal
class Dog(Animal):
    def __init__(self, name, weight, height,color, kind):
        super().__init__(name, weight, height)
        self.color = color
        self.kind = kind
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def set_weight(self, weight):
        self._weight = weight
    def show(self):
        # print(f"This is {self._name} with weight={self._weight} and height={self._height}")
        print("This is {} with weight {} and height {} màu lông: {}  Giống: {}".format(self._name,self._weight, self._height,self.color, self.kind))
if __name__ == '__main__':
    dog = Dog("meo", 30, 50, "đỏ", "becge")
    dog.show()
