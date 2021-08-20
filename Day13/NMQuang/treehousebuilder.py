from builder import Builder
from treehouse import TreeHouse


class TreeHouseBuilder(Builder):
    def __init__(self):
        self._result = TreeHouse()
