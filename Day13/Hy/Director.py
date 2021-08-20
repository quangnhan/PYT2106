from BuilderTreeHouse import BuilderTreeHouse
class Director:
    def __init__(self, builder):
        self.__builder = builder

    def make(self,house_type):
        if house_type == "classic":
            self.__builder.build_walls(8)
            self.__builder.build_doors(2)
            self.__builder.build_windows(6)
        elif house_type == "mordern":
            self.__builder.build_walls(40)
            self.__builder.build_doors(2)
            self.__builder.build_windows(60)