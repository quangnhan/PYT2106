from treehouse import TreeHouse


class TreeHouseBuilder:
    def __init__(self):
        self.__result = TreeHouse()
    
    def build_wall(self, number):
        self.__result.walls = number

    def build_door(self, number):
        self.__result.doors = number

    def build_window(self, number):
        self.__result.windows = number

    def get_result(self):
        return self.__result
