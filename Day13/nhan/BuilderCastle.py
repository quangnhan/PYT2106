from Builder import Builder
from Castle import Castle

class BuilderCastle(Builder):
    def __init__(self):
        self._result = Castle()

    def build_pool(self, number):
        self._result.pool = number
    