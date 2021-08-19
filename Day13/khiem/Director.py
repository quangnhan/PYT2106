
class Director:
    def __init__(self, builder):
        self.__builder = builder

    def make(self, type_house):
        if type_house == "easy":
            print('easy')
            self.__builder.build_walls(4)
            self.__builder.build_doors(2)
            self.__builder.build_windowns(3)
        elif type_house == "normal":
            print('normal')
            self.__builder.build_walls(15)
            self.__builder.build_doors(4)
            self.__builder.build_windowns(10)