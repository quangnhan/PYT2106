class Director:
    def __init__(self, personel):
        self.__result = personel

    def make(self, house_type):
        if house_type == 'classic':
            self.__result.build_wall(4) 
            self.__result.build_door(2) 
            self.__result.build_window(6) 

        elif house_type == 'modern':
            self.__result.build_wall(12) 
            self.__result.build_door(3) 
            self.__result.build_window(20) 
