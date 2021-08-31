from mordernHouse import MordernHouse

class BuilderMordernHouse:
    __result = MordernHouse()
    
    def build_doors(self, number):
        self.__result.doors = number

    def build_windows(self, number):
        self.__result.windows = number

    def build_walls(self, number):
        self.__result.walls = number

    def show(self):
        self.__result.show()