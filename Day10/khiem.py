from animal import Animal

class Chicken(Animal):
    def __init__(self, name, weight, height):
        super().__init__(name, weight, height)



if __name__ == '__main__':
    chiken = Chicken('chiquaqua', 10, 20)
    chiken.show()
    