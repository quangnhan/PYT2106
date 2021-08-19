class Builder:
    _result = None

    def build_walls(self, number):
        self._result.walls = number

    def build_doors(self, number):
        self._result.doors = number

    def build_windows(self, number):
        self._result.windows = number
        
    def build_pool(self, number):
        pass
    
    def get_result(self):
        return self._result