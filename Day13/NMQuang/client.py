from treehousebuilder import TreeHouseBuilder
from castlebuilder import CastleBuilder
from director import Director

houseBuilder = TreeHouseBuilder()
myHouse = houseBuilder.get_result()
myDesigner = Director(houseBuilder)
myDesigner.make('classic')

myHouse.show()

castleBuilder = CastleBuilder()
myCastle = castleBuilder.get_result()
myCompany = Director(castleBuilder)
myCompany.make('modern')

myCastle.show()
