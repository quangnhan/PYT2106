from BuilderStonesHouse import BuilderStonesHouse
from Director import Director

builder = BuilderStonesHouse()
director = Director(builder)
print('Stones from director')
director.make("normal")
house = builder.get_result()
house.show()
