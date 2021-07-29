class Animal:
    def __init__(self, name, weight, height):
        self.__name = name
        self.__weight = weight
        self.__height = height

    def get_name(self):
        return self.__name

    def show(self):
        print(f"This is {self.__name} with weight={self.__weight} and height={self.__height}")

    def shout(self):
        print("rrrrrrrrrrrr")

    def combo(self):
        self.show()
        self.shout()

if __name__ == "__main__":
    lion = Animal("Lion", 100, 50)
    lion.show()
    lion.shout()
    lion.combo()
