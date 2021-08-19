from Director import Director
from BuilderTreeHouse import BuilderTreeHouse
from BuilderCastle import BuilderCastle
from BuilderDiamond import BuilderDiamond


# builder = BuilderTreeHouse()
# builder = BuilderCastle()
builder = BuilderDiamond()

house = builder.get_result()
director = Director(builder)

director.make("mordern")

house.show()