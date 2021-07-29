from animal import Animal
class Dog(Animal):
    def __init__(self, name, weight, height,color, kind):
        super().__init__(name, weight, height)
        self.color = color,
        self.kind = kind
    def set_name(self, name):
        self._name = name
    def set_weight(self, weight):
        self._weight = weight
    def show():
        print(f"This is {self._name} with weight={self._weight} and height={self._height}")
        print("màu lông: {} , Giống: ".format(self.color, self.kind))
if __name__ == '__main__':
    dog = Dog("meo", 30, 50, "đỏ", "becge")
    dog.show()
