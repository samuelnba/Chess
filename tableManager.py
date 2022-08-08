class Table():
    current = ""
    def __init__(self):
        self.tableLogic = [[ Rook("00", "W"), Knight("01", "W"), Bishop("02", "W"), Queen("03", "W"), King("04", "W"), Bishop("05", "W"), Knight("06", "W"), Rook("07", "W")],
                           [ Pawn("10", "W"), Pawn("11", "W"), Pawn("12", "W"), Pawn("13", "W"), Pawn("14", "W"), Pawn("15", "W"), Pawn("16", "W"), Pawn("17", "W")],
                           [ Empty("20", "N"), Empty("21", "N"), Empty("22", "N"), Empty("23", "N"), Empty("24", "N"), Empty("25", "N"), Empty("26", "N"), Empty("27", "N")],
                           [ Empty("30", "N"), Empty("31", "N"), Empty("32", "N"), Empty("33", "N"), Empty("34", "N"), Empty("35", "N"), Empty("36", "N"), Empty("37", "N")],
                           [ Empty("40", "N"), Empty("41", "N"), Empty("42", "N"), Empty("43", "N"), Empty("44", "N"), Empty("45", "N"), Empty("46", "N"), Empty("47", "N")],
                           [ Empty("50", "N"), Empty("51", "N"), Empty("52", "N"), Empty("53", "N"), Empty("54", "N"), Empty("55", "N"), Empty("56", "N"), Empty("57", "N")],
                           [ Pawn("60", "B"), Pawn("61", "B"), Pawn("62", "B"), Pawn("63", "B"), Pawn("64", "B"), Pawn("65", "B"), Pawn("66", "B"), Pawn("67", "B")],
                           [ Rook("70", "B"), Knight("71", "B"), Bishop("72", "B"), Queen("73", "B"), King("74", "B"), Bishop("75", "B"), Knight("76", "B"), Rook("77", "B")]] 
    
    @classmethod
    def newTable(cls):
        Table.current = Table()

# / --------------- \
#  Figure Prototypes 
# \ --------------- /

class Figure():
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def __str__(self):
        return self.fiType

class Empty(Figure):
    fiType = "  "
    def __init__(self, position, color):
        super().__init__(position, color)
        self.fiType = Empty.fiType

class Rook(Figure):
    fiType = "RO"
    movement = [[0, 1, True], [0, -1, True], [-1, 0, True], [1, 0, True]]

    def __init__(self, position, color):
        super().__init__(position, color)
        self.fiType = Rook.fiType

class Knight(Figure):
    fiType = "KN"
    movement = [[-1, 2, False], [-2, 1, False], [-2, -1, False], [-1, -2, False], [1, -2, False], [2, -1, False], [2, 1, False], [1, 2, False]]
    
    def __init__(self, position, color):
        super().__init__(position, color)
        self.fiType = Knight.fiType

class Bishop(Figure):
    fiType = "BI"
    movement = [[-1, 1, True], [1, 1, True], [-1, -1, True], [+1, -1, True]]

    def __init__(self, position, color):
        super().__init__(position, color)
        self.fiType = Bishop.fiType

class Queen(Figure):
    fiType = "QU"
    movement = [[0, 1, False], [-1, 1, False], [-1, 0, False], [-1, -1, False], [0, -1, False], [1, -1, False], [1, 0, False], [1, 1, False],
                      [0, 1, True], [0, -1, True], [-1, 0, True], [1, 0, True], [-1, 1, True], [1, 1, True], [-1, -1, True], [+1, -1, True]]

    def __init__(self, position, color):
        super().__init__(position, color)
        self.fiType = Queen.fiType

class King(Figure):
    fiType = "KI"
    movement = [[0, 1, False], [-1, 1, False], [-1, 0, False], [-1, -1, False], [0, -1, False], [1, -1, False], [1, 0, False], [1, 1, False]]

    def __init__(self, position, color):
        super().__init__(position, color)
        self.fiType = King.fiType

class Pawn(Figure):
    fiType = "PA"
    movement = [[0, 1, False], [0, 2, False]]
    
    def __init__(self, position, color):
        super().__init__(position, color)
        self.fiType = Pawn.fiType

a = Table()
print(a.tableLogic[0][3])