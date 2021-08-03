from animal import Animal

class Peguin(Animal):
    def __init__(self, name, weight, height, age):
        super().__init__(name, weight, height)
        self.age: int = age
        

    # def get_name(self):
    #     return self._name

    def showInfo(self):
        print(f'Name: {self._name}\nWeight: {self._weight}\nHeight: {self._height}\nAge: {self.age}')

    def shout(self):
        print('Fight me!')

if __name__ == "__main__":
     myPeguin = Peguin('Loco', 30, 40, 5)
     print(myPeguin.showInfo())
     myPeguin.shout()