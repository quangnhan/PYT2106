from animal import Animal

class Peguin(Animal):
    def __init__(self, name, weight, height, leg, color):
        super().__init__(name, weight, height)
        self.leg = leg
        self.color = color

    def show(self):
        print(f"Agent: {self._name}")

    def set_name(self, name):
        self._name = name

    def show(self):
        print(f"Agent: {self._name}")

    def get_leg(self):
        return self.leg

    def get_color(self):
        return self.color


if __name__ == "__main__":
    p1 = Peguin("Loco", 50, 40, 2, "pink")
    #p1.show()
    p1(Peguin.get_leg())
    p1(Peguin.get_colour())