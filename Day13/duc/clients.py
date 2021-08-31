from BuilderHouse import BuilderHouse
from Director import Director

# builder = BuilderHouse()
builder = BuilderCastle()
director = Director(builder)
director.make("mordern")

house = builder.get_result()
house.show()