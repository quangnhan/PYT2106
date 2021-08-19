from Director import Director
from BuilderTreeHouse import BuilderTreeHouse
from BuilderCastle import BuilderCastle

# builder = BuilderTreeHouse()
builder = BuilderCastle()
house = builder.get_result()
director = Director(builder)

director.make("mordern")

house.show()