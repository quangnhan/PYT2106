from StonesHouse import StonesHouse

class BuilderStonesHouse:
    def __init__(self):
        self.__result = StonesHouse()

    def build_walls(self, number):
        self.__result.walls = number

    def build_windowns(self, number):
        self.__result.windowns = number

    def build_doors(self, number):
        self.__result.doors = number

    def get_result(self):
        return self.__result
