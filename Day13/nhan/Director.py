class Director:
    def __init__(self, builder):
        self.__builder = builder

    def make(self, house_type):
        if house_type == "classic":
            self.__builder.build_walls(4)
            self.__builder.build_doors(2)
            self.__builder.build_windows(3)
        elif house_type == "mordern":
            self.__builder.build_walls(20)
            self.__builder.build_doors(5)
            self.__builder.build_windows(50)
            self.__builder.build_pool(1)