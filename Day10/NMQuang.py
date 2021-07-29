from animal import Animal


class Cat(Animal):
    def __init__(self, name, weight, height, age, colour):
        super().__init__(name, weight, height)
        self.age: int = age
        self.colour: str = colour

    def get_weight(self):
        return self._weight

    def get_height(self):
        return self._height

    def get_age(self):
        return self.age

    def get_colour(self):
        return self.colour

    def shout(self):
        print('Meow~~!')


def main():
    myCat = Cat('Nyan', 2, 50, 5, 'Golden')
    print(myCat.get_weight())
    print(myCat.get_height())
    print(myCat.get_age())
    print(myCat.get_colour())
    myCat.shout()
    print(myCat.show())


if __name__ == "__main__":
    main()
