from Builder import Builder
from Castle import Castle

class BuilderCastle(Builder):
    def __init__(self, get_result):
        super().__init__(build_walls, build_windows, build_doors, build_pools)
        self.get_result
        return Builder.get_result