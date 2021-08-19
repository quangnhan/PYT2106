from BuilderTreeHouse import BuilderTreeHouse
from Director import Director

builder = BuilderTreeHouse()
director = Director(builder)
director.make("mordern")

house = builder.get_result()
house.show()