class Director:
    def __init__(self, builder):
        self.__builder = builder

    def make(self, build_type):
        print(f"Design by {build_type}")
        if build_type == 'classic':
            self.__builder.build_walls(4)
            self.__builder.build_doors(1)
            self.__builder.build_windows(1)
        elif build_type == 'mordern':
            self.__builder.build_walls(44)
            self.__builder.build_doors(11)
            self.__builder.build_windows(11)