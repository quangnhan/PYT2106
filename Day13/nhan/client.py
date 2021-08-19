from BuilderTreeHouse import BuilderTreeHouse
from BuilderCastle import BuilderCastle
from Director import Director

# builder = BuilderTreeHouse()
builder = BuilderCastle()
director = Director(builder)
director.make("mordern")

house = builder.get_result()
house.show()