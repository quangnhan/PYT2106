from Director import Director
from BuilderTreeHouse import BuilderTreeHouse


builder = BuilderTreeHouse()
house = builder.get_result()
director = Director(builder)

director.make("mordern")

house.show()