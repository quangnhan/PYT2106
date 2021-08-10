from animal import Animal

class Chicken(Animal):
    def __init__(self, name, weight, height, age, rank_number):
        super().__init__(name, weight, height)
        self.age = age
        self.rank_number = rank_number

    def fly(self):
        print('Can fly low range')

    def rating_animal(self,age, rank_number):
        if rank_number ==1:
            print(f'Wellcom {self._name} the Champion with age {self.age}')
        else:
            print(f'The {self._name} is not champion')

    def shout(self):
        print(' O O O O O O O O')



if __name__ == '__main__':
    chicken = Chicken('chiquaqua', 10, 20, 1, 1)
    chicken.show()
    chicken.rating_animal(2,2)
    chicken.shout()
    
    