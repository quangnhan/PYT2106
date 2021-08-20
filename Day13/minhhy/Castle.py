class Castle:
    walls = 0
    windows = 0
    doors = 0
    pools = 0

    def show(self):
        print(f"[DEBUG] Castle had {self.walls} walls, {self.windows} windows, {self.doors} doors, {self.pools} pools")