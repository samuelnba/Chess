# Colors( BLUE: "\u001b[34m"; WHITE: "\u001b[37m"; GREEN: "\033[92m"; RED: "\033[31m" )

from unittest import skip


logic = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]

logic2 = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]


tableHelp = """
+----+----+----+----+----+----+----+----+
| a8 | b8 | c8 | d8 | e8 | f8 | g8 | h8 |
+----+----+----+----+----+----+----+----+
| a7 | b7 | c7 | d7 | e7 | f7 | g7 | h7 |
+----+----+----+----+----+----+----+----+
| a6 | b6 | c6 | d6 | e6 | f6 | g6 | h6 |
+----+----+----+----+----+----+----+----+
| a5 | b5 | c5 | d5 | e5 | f5 | g5 | h5 |
+----+----+----+----+----+----+----+----+
| a4 | b4 | c4 | d4 | e4 | f4 | g4 | h4 |
+----+----+----+----+----+----+----+----+
| a3 | b3 | c3 | d3 | e3 | f3 | g3 | h3 |
+----+----+----+----+----+----+----+----+
| a2 | b2 | c2 | d2 | e2 | f2 | g2 | h2 |
+----+----+----+----+----+----+----+----+
| a1 | b1 | c1 | d1 | e1 | f1 | g1 | h1 |
+----+----+----+----+----+----+----+----+
"""


class Figure():
    def __init__(self, type, position, color, steps):
        self.type = type
        self.position = position
        self.color = color
        self.steps = steps


def tableBuilder():
    return f"""
  +----+----+----+----+----+----+----+----+
H | {logic[0][7]} | {logic[1][7]} | {logic[2][7]} | {logic[3][7]} | {logic[4][7]} | {logic[5][7]} | {logic[6][7]} | {logic[7][7]} |
  +----+----+----+----+----+----+----+----+
G | {logic[0][6]} | {logic[1][6]} | {logic[2][6]} | {logic[3][6]} | {logic[4][6]} | {logic[5][6]} | {logic[6][6]} | {logic[7][6]} |
  +----+----+----+----+----+----+----+----+
F | {logic[0][5]} | {logic[1][5]} | {logic[2][5]} | {logic[3][5]} | {logic[4][5]} | {logic[5][5]} | {logic[6][5]} | {logic[7][5]} |
  +----+----+----+----+----+----+----+----+
E | {logic[0][4]} | {logic[1][4]} | {logic[2][4]} | {logic[3][4]} | {logic[4][4]} | {logic[5][4]} | {logic[6][4]} | {logic[7][4]} |
  +----+----+----+----+----+----+----+----+
D | {logic[0][3]} | {logic[1][3]} | {logic[2][3]} | {logic[3][3]} | {logic[4][3]} | {logic[5][3]} | {logic[6][3]} | {logic[7][3]} |
  +----+----+----+----+----+----+----+----+
C | {logic[0][2]} | {logic[1][2]} | {logic[2][2]} | {logic[3][2]} | {logic[4][2]} | {logic[5][2]} | {logic[6][2]} | {logic[7][2]} |
  +----+----+----+----+----+----+----+----+
B | {logic[0][1]} | {logic[1][1]} | {logic[2][1]} | {logic[3][1]} | {logic[4][1]} | {logic[5][1]} | {logic[6][1]} | {logic[7][1]} |
  +----+----+----+----+----+----+----+----+
A | {logic[0][0]} | {logic[1][0]} | {logic[2][0]} | {logic[3][0]} | {logic[4][0]} | {logic[5][0]} | {logic[6][0]} | {logic[7][0]} |
  +----+----+----+----+----+----+----+----+
    1    2    3    4    5    6    7    8
"""


def checkIfFree(toCheck):
    if logic[toCheck[0]][toCheck[1]] == "  ":
        return True
    else:
        return False


def checkTheColor(position, color):
    if logic2[position[0]][position[1]].color == color:
        return True
    else:
        return False


def letterToNumber(letter):
    letter = letter.lower()
    if letter == "a":
        return 0
    elif letter == "b":
        return 1
    elif letter == "c":
        return 2
    elif letter == "d":
        return 3
    elif letter == "e":
        return 4
    elif letter == "f":
        return 5
    elif letter == "g":
        return 6
    elif letter == "h":
        return 7
    else:
        print(
            "\033[31m" + "You should use a command that exists!" + "\u001b[37m")
        return False


def numberToLetter(number):
    number = int(number)
    if number == 0:
        return "A"
    elif number == 1:
        return "B"
    elif number == 2:
        return "C"
    elif number == 3:
        return "D"
    elif number == 4:
        return "E"
    elif number == 5:
        return "F"
    elif number == 6:
        return "G"
    elif number == 7:
        return "H"
    else:
        print(
            "\033[31m" + "You should use a command that exists!" + "\u001b[37m")
        return False

# def kill(figure):
#     if figure == "pa":
        

def availableSteps(position, figure, color, steps):
    figures = {"pa": [[0, 1, False], [0, 2, False]],
               "bi": [[-1, 1, True], [1, 1, True], [-1, -1, True], [+1, -1, True]],
               "kn": [[-1, 2, False], [-2, 1, False], [-2, -1, False], [-1, -2, False], [1, -2, False], [2, -1, False], [2, 1, False], [1, 2, False]],
               "ro": [[0, 1, True], [0, -1, True], [-1, 0, True], [1, 0, True]],
               "ki": [[0, 1, False], [-1, 1, False], [-1, 0, False], [-1, -1, False], [0, -1, False], [1, -1, False], [1, 0, False], [1, 1, False]],
               "qu": [[0, 1, False], [-1, 1, False], [-1, 0, False], [-1, -1, False], [0, -1, False], [1, -1, False], [1, 0, False], [1, 1, False],
                      [0, 1, True], [0, -1, True], [-1, 0, True], [1, 0, True], [-1, 1, True], [1, 1, True], [-1, -1, True], [+1, -1, True]]}
    availables = []
    for i in figures[figure]:
        temp = position.copy()
        if i[2] == False:
            if color:
                temp[0] = temp[0] + i[0]
                temp[1] = temp[1] + i[1]
            else:
                temp[0] = temp[0] - i[0]
                temp[1] = temp[1] - i[1]
            if temp[0] > 7 or temp[0] < 0 or temp[1] > 7 or temp[1] < 0:
                skip
            else:
                if checkIfFree(temp):
                    availables.append(temp)
            if figure == "pa":
                if steps > 0:
                    break
        elif i[2] == True:
            counter = 1
            while True:
                temp = position.copy()
                if color:
                    temp[0] = temp[0] + i[0] * counter
                    temp[1] = temp[1] + i[1] * counter
                else:
                    temp[0] = temp[0] - i[0] * counter
                    temp[1] = temp[1] - i[1] * counter
                counter += 1
                if temp[0] == 8 or temp[0] == -1 or temp[1] == 8 or temp[1] == -1:
                    break
                if checkIfFree(temp):
                    availables.append(temp)
                else:
                    break
    temp_list = []
    for i in availables:
        if i not in temp_list:
            temp_list.append(i)
    availables = temp_list
    if availables == []:
        print("No available steps, choose another figure")
        return []
    return availables


def spawn():
    temp = [['ro', [0, 7], False], ['kn', [1, 7], False], ['bi', [2, 7], False], ['ki', [3, 7], False], ['qu', [4, 7], False], ['bi', [5, 7], False], ['kn', [6, 7], False],
            ['ro', [7, 7], False], ['pa', [0, 6], False], ['pa', [1, 6], False], ['pa', [
                2, 6], False], ['pa', [3, 6], False], ['pa', [4, 6], False], ['pa', [5, 6], False],
            ['pa', [6, 6], False], ['pa', [7, 6], False]]

    temp2 = [['ro', [0, 0], True], ['kn', [1, 0], True], ['bi', [2, 0], True], ['ki', [3, 0], True], ['qu', [4, 0], True], ['bi', [5, 0], True], ['kn', [6, 0], True],
             ['ro', [7, 0], True], ['pa', [0, 1], True], ['pa', [1, 1], True], ['pa', [
                 2, 1], True], ['pa', [3, 1], True], ['pa', [4, 1], True], ['pa', [5, 1], True],
             ['pa', [6, 1], True], ['pa', [7, 1], True]]

    spawned = []
    for i in temp:
        spawned.append(Figure(i[0], i[1], i[2], 0))
    for i in temp2:
        spawned.append(Figure(i[0], i[1], i[2], 0))

    for i in range(len(spawned)):
        logic2[spawned[i].position[0]][spawned[i].position[1]] = spawned[i]
        if spawned[i].color == False:
            logic[spawned[i].position[0]][spawned[i].position[1]
                                          ] = "\u001b[34m" + spawned[i].type + "\u001b[37m"
        else:
            logic[spawned[i].position[0]
                  ][spawned[i].position[1]] = spawned[i].type
        


def help():
    commands = ['help', 'focus [position X] [position Y]']
    print("\033[92m" + f"Commands: ")
    for i in commands:
        print(i)

    print("\u001b[37m")


def focus(todo, color):
    if todo[1] < 8 and todo[2] < 8 and todo[1] > -1 and todo[2] > -1:
        if checkIfFree([todo[1], todo[2]]):
            print(
                "\033[31m" + "You have to focus on a position with a figure" + "\u001b[37m")
            return False
        else:
            if checkTheColor([todo[1], todo[2]], color):
                l1 = logic[todo[1]][todo[2]]
                l2 = logic2[todo[1]][todo[2]]
                availables = availableSteps([todo[1], todo[2]],
                                            logic2[todo[1]][todo[2]].type, logic2[todo[1]][todo[2]].color, logic2[todo[1]][todo[2]].steps)
                availablesH = []
                if availables == []:
                    return False
                logic2[todo[1]][todo[2]].steps += 1
                for array in range(len(availables)):
                    temp = []
                    for number in range(len(availables[array])):
                        temp.append(availables[array][number] + 1)
                    availablesH.append(temp)
                for i in range(len(availablesH)):
                    temp = numberToLetter(availablesH[i][1] - 1)
                    availablesH[i][1] = availablesH[i][0]
                    availablesH[i][0] = temp
                print("\033[92m")
                for i in availablesH:
                    print(i[0] + str(i[1]))
                print("\u001b[37m")
                moveTo = int(input(
                    "\033[92m" + 'Write the number of the position you want to move to! ' + "\u001b[37m"))
                if moveTo <= len(availables):
                    logic2[todo[1]][todo[2]].position = availables[moveTo - 1]
                    logic2[availables[moveTo - 1][0]][availables[moveTo - 1]
                                                      [1]] = logic2[todo[1]][todo[2]]
                    logic2[todo[1]][todo[2]] = '  '
                    logic[availables[moveTo - 1][0]][availables[moveTo - 1]
                                                     [1]] = logic[todo[1]][todo[2]]
                    logic[todo[1]][todo[2]] = '  '
                    return True
                else:
                    print(
                        "\033[31m" + "The list does not contain that!" + "\u001b[37m")
                    return False
            else:
                print(
                    "\033[31m" + "You have to choose a figure of your own color!" + "\u001b[37m")
                return False
    else:
        print(
            "\033[31m" + "Positions should be between the number '0' and '8'" + "\u001b[37m")
        return False


def main():
    commands = ['help', 'focus [position]']
    player = True
    spawn()
    while True:
        print(tableBuilder())

        if player:
            print("\033[92m" + "Player: White" + "\u001b[37m")
        else:
            print("\033[92m" + "Player: Blue" + "\u001b[37m")
        while True:
            todo = input(
                "\033[92m" + "Make any action! ('help' for help) " + "\u001b[37m").lower()
            todo = todo.split()
            if todo[0] == 'help':
                help()
            elif todo[0] == 'focus':
                if len(todo) == 3:
                    temp = letterToNumber(todo[1])
                    todo[1] = int(todo[2]) - 1
                    todo[2] = temp
                    if focus(todo, player):
                        player = not player
                        break
                else:
                    print(
                        "\033[31m" + "'focus' should be used this way: 'focus [position X] [position Y]' {e.g. 'focus 4 3'" + "\u001b[37m")
            else:
                print(
                    "\033[31m" + "You should use a command that exists!" + "\u001b[37m")


if __name__ == "__main__":
    main()
