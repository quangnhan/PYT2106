from Builder import Builder
from TreeHouse import TreeHouse

class BuilderTreeHouse(Builder):
    def __init__(self):
        self._result = TreeHouse()