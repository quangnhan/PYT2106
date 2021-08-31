class Builder:
    _result = None

    def build_wall(self, number):
        self._result.walls = number

    def build_door(self, number):
        self._result.doors = number

    def build_window(self, number):
        self._result.windows = number

    def get_result(self):
        return self._result
