import tableManager

class Movement():
    def __init__(self):
        pass    

    def move(positionFrom, positionTo):
        tableManager.Table.current.tableLogic[int(positionTo[0])][int(positionTo[1])] = tableManager.Table.current.tableLogic[int(positionFrom[0])][int(positionFrom[1])]
        tableManager.Table.current.tableLogic[int(positionFrom[0])][int(positionTo[1])] = tableManager.Empty(str(positionFrom[0]) + str(positionFrom[1]), "N") 

# tableManager.Table.newTable()
# print(tableManager.Table.printTable())
# Movement.move("61", "51")
