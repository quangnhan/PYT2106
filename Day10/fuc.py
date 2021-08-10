from animal import Animal

class duck(Animal):
    def __init__(self, name, weight, height, color, num_legs):
        super().__init__(name, weight, height)
        self.color = color
        self.num_legs = num_legs
    
    def show(self):
        print(f"This is {self._name} with weight={self._weight} and height={self._height}, color: {self.color}, num legs: {self.num_legs}")

    def sound(self):
        print('quảk')
    
    def eat(self):
        print('eating')
    
    def call(self):
        print(f'Hey! {self._name}')
    

if __name__ == '__main__':
    duck1= duck('donald', '85kg', '180cm', 'white', 3)
    duck1.show()
    duck1.sound()
    duck1.eat()
    duck1.call()
