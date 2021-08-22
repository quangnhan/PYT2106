from builderMordernHouse import BuilderMordernHouse
from builderTreeHouse import BuilderTreeHouse

class Builder:
    def __init__(self, builder_type):
        if builder_type == 'treehouse':
            self.builder = BuilderTreeHouse()
        elif builder_type == 'mordernhouse':
            self.builder = BuilderMordernHouse()
        else:
            print('so such type house')

    def build_doors(self, number):
        self.builder.build_doors(number)

    def build_windows(self, number):
        self.builder.build_windows(number)

    def build_walls(self, number):
        self.builder.build_walls(number)

    def show(self):
        self.builder.show()