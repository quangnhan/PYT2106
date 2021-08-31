class Director:
    def __init__(self, builder):
        self.__builder = builder

    def make(self, build_type):
        print("Design by {build_type}")
        if build_type == 'classic':
            self.__builder.build_wall(4)
            self.__builder.build_door(1)
            self.__builder.build_window(1)
        elif build_type == 'mordern':
            self.__builder.build_wall(44)
            self.__builder.build_door(11)
            self.__builder.build_window(11)