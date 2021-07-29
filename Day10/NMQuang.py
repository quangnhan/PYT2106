from animal import Animal


class Cat(Animal):
    def __init__(self, name, weight, height):
        super().__init__(name, weight, height)


def main():
    myCat = Cat('Nyan', 2, 50)
    myCat.show()


if __name__ == "__main__":
    main()
