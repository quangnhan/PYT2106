from builderTreeHouse import BuilderTreeHouse
from builderMordernHouse import BuilderMordernHouse
from builder import Builder

class Director:
    def __init__(self, type_house):
        self.builder = Builder(type_house)

    def make(self):
        self.builder.build_doors(5)

    def show(self):
        self.builder.show()
        