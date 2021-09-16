class Builder:
    def __init__(self):
        self.__result = Builder()

    def build_walls(self, number):
        self.__result.walls = number

    def build_doors(self, number):
        self.__result.doors = number

    def build_windows(self, number):
        self.__result.windows = number

    def build_pools(self, number):
        self.__result.pools = number

    def get_result(self):
        return self.__result