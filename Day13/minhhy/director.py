class Director:
    def __init__(self, builder):
        self.__builder = builder

    def make(self, house_type):
        print(f"[DEBUG] director type: {house_type}")
        if house_type == 'classic':
            self.__builder.build_wall(4)
            self.__builder.build_door(2)
            self.__builder.build_window(3)
        elif house_type == 'mordern':
            self.__builder.build_wall(20)
            self.__builder.build_door(20)
            self.__builder.build_window(20)
            self.__builder.build_pool(1)
        else:
            raise  Exception('[ERROR] input wrong type')
