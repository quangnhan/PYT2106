from TreeHouse import TreeHouse
from Builder import Builder

class BuilderTreeHouse(Builder):
    def __init__(self):
        self._result = TreeHouse()
