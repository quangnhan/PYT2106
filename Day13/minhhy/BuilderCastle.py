from Castle import Castle
from Builder import Builder

class BuilderCastle(Builder):
    def __init__(self):
        self._result = Castle()

    def build_pool(self, number):
        self._result.pools = number
