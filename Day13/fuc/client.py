from builderTreeHouse import BuilderTreeHouse
from director import Director

class Client:
    def __init__(self, director):
        self.director = director

    def make(self):
        self.director.make()

    def show(self):
        self.director.show()


if __name__ =="__main__":
    director =Director('mordernhouse')
    fuc = Client(director)
    fuc.make()
    fuc.show()