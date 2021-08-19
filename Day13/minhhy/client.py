from BuilderTreeHouse import BuilderTreeHouse
from director import Director

builder = BuilderTreeHouse()

# first treehouse
print("[DEBUG] -- first tree house")
builder.build_wall(4)
builder.build_door(2)
builder.build_window(3)

house = builder.get_result()
house.show()

# second treehouse
print("[DEBUG] -- second tree house")
builder.build_wall(10)
builder.build_window(30)

house = builder.get_result()
house.show()

# director
print("[DEBUG] -- director")
director = Director(builder)
director.make('mordern')
house = builder.get_result()
house.show()