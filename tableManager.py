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

    @classmethod
    def printTable(cls):
        return f"""
                  +----+----+----+----+----+----+----+----+
                H | {Table.current.tableLogic[0][0]} | {Table.current.tableLogic[0][1]} | {Table.current.tableLogic[0][2]} | {Table.current.tableLogic[0][3]} | {Table.current.tableLogic[0][4]} | {Table.current.tableLogic[0][5]} | {Table.current.tableLogic[0][6]} | {Table.current.tableLogic[0][7]} |
                  +----+----+----+----+----+----+----+----+
                G | {Table.current.tableLogic[1][0]} | {Table.current.tableLogic[1][1]} | {Table.current.tableLogic[1][2]} | {Table.current.tableLogic[1][3]} | {Table.current.tableLogic[1][4]} | {Table.current.tableLogic[1][5]} | {Table.current.tableLogic[1][6]} | {Table.current.tableLogic[1][7]} |
                  +----+----+----+----+----+----+----+----+
                F | {Table.current.tableLogic[2][0]} | {Table.current.tableLogic[2][1]} | {Table.current.tableLogic[2][2]} | {Table.current.tableLogic[2][3]} | {Table.current.tableLogic[2][4]} | {Table.current.tableLogic[2][5]} | {Table.current.tableLogic[2][6]} | {Table.current.tableLogic[2][7]} |
                  +----+----+----+----+----+----+----+----+
                E | {Table.current.tableLogic[3][0]} | {Table.current.tableLogic[3][1]} | {Table.current.tableLogic[3][2]} | {Table.current.tableLogic[3][3]} | {Table.current.tableLogic[3][4]} | {Table.current.tableLogic[3][5]} | {Table.current.tableLogic[3][6]} | {Table.current.tableLogic[3][7]} |
                  +----+----+----+----+----+----+----+----+
                D | {Table.current.tableLogic[4][0]} | {Table.current.tableLogic[4][1]} | {Table.current.tableLogic[4][2]} | {Table.current.tableLogic[4][3]} | {Table.current.tableLogic[4][4]} | {Table.current.tableLogic[4][5]} | {Table.current.tableLogic[4][6]} | {Table.current.tableLogic[4][7]} |
                  +----+----+----+----+----+----+----+----+
                C | {Table.current.tableLogic[5][0]} | {Table.current.tableLogic[5][1]} | {Table.current.tableLogic[5][2]} | {Table.current.tableLogic[5][3]} | {Table.current.tableLogic[5][4]} | {Table.current.tableLogic[5][5]} | {Table.current.tableLogic[5][6]} | {Table.current.tableLogic[5][7]} |
                  +----+----+----+----+----+----+----+----+
                B | {Table.current.tableLogic[6][0]} | {Table.current.tableLogic[6][1]} | {Table.current.tableLogic[6][2]} | {Table.current.tableLogic[6][3]} | {Table.current.tableLogic[6][4]} | {Table.current.tableLogic[6][5]} | {Table.current.tableLogic[6][6]} | {Table.current.tableLogic[6][7]} |
                  +----+----+----+----+----+----+----+----+
                A | {Table.current.tableLogic[7][0]} | {Table.current.tableLogic[7][1]} | {Table.current.tableLogic[7][2]} | {Table.current.tableLogic[7][3]} | {Table.current.tableLogic[7][4]} | {Table.current.tableLogic[7][5]} | {Table.current.tableLogic[7][6]} | {Table.current.tableLogic[7][7]} |
                  +----+----+----+----+----+----+----+----+
                    1    2    3    4    5    6    7    8
                """

# / --------------- \
#  Figure Prototypes 
# \ --------------- /

class Figure():
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def __str__(self):
        if self.color == "B":
            return "\u001b[34m" + self.fiType + "\u001b[37m"
        return self.fiType

class Empty(Figure):
    fiType = "  "
    def __init__(self, position, color):
        super().__init__(position, color)

class Rook(Figure):
    fiType = "RO"
    movement = [[0, 1, True], [0, -1, True], [-1, 0, True], [1, 0, True]]

    def __init__(self, position, color):
        super().__init__(position, color)

class Knight(Figure):
    fiType = "KN"
    movement = [[-1, 2, False], [-2, 1, False], [-2, -1, False], [-1, -2, False], [1, -2, False], [2, -1, False], [2, 1, False], [1, 2, False]]
    
    def __init__(self, position, color):
        super().__init__(position, color)

class Bishop(Figure):
    fiType = "BI"
    movement = [[-1, 1, True], [1, 1, True], [-1, -1, True], [+1, -1, True]]

    def __init__(self, position, color):
        super().__init__(position, color)

class Queen(Figure):
    fiType = "QU"
    movement = [[0, 1, False], [-1, 1, False], [-1, 0, False], [-1, -1, False], [0, -1, False], [1, -1, False], [1, 0, False], [1, 1, False],
                      [0, 1, True], [0, -1, True], [-1, 0, True], [1, 0, True], [-1, 1, True], [1, 1, True], [-1, -1, True], [+1, -1, True]]

    def __init__(self, position, color):
        super().__init__(position, color)
class King(Figure):
    fiType = "KI"
    movement = [[0, 1, False], [-1, 1, False], [-1, 0, False], [-1, -1, False], [0, -1, False], [1, -1, False], [1, 0, False], [1, 1, False]]

    def __init__(self, position, color):
        super().__init__(position, color)

class Pawn(Figure):
    fiType = "PA"
    movement = [[0, 1, False], [0, 2, False]]
    
    def __init__(self, position, color):
        super().__init__(position, color)


Table.newTable()
print(Table.printTable())