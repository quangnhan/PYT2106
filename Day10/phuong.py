from animal import Animal

class Peguin(Animal):
    def __init__(self, name, weight, height):
        super().__init__(name, weight, height)

    def show(self):
        print(f"Agent: {self._name}")

    def set_name(self, name):
        self._name = name

if __name__ == "__main__":
    peguin = Peguin("Loco", 50, 40)
    peguin.show()