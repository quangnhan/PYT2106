from treehouse import TreeHouse
from treehousebuilder import TreeHouseBuilder
from director import Director

houseBuilder = TreeHouseBuilder()
myHouse = houseBuilder.get_result()
myDesigner = Director(houseBuilder)

myDesigner.make('modern')

myHouse.show()
