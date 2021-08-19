from Castle import Castle
from Builder import Builder

class BuilderCastle(Builder):
    def __init__(self):
        self._result = Castle()

    # overwrite build_pool from Builder
    def build_pool(self, number):
        self._result.pools = number
