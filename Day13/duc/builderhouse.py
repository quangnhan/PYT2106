from House import House

class builderHouse:
     def _init_(self):
         self._result = House()
    
    def build_walls(self, number):
        self.__result.walls = number

    def build_doors(self, number):
        self.__result.doors = number

    def build_windows(self, number):
        self.__result.windows = number

    def get_result(self):
        return self.__result