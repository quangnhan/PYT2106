from animal import Animal

class Dog(Animal):
    def __init__(self,name,weight,height):
        super().__init__(name, weight,height)


if __name__ == "__main__":
    dog = Dog("Lucky", 100, 45)
    dog.show()