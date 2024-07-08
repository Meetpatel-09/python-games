player1Name = ""
player2Name = ""
playerTurn = 1
maxTurn = 9
turnCounter = 0
isNotWin = True

matrix = [
    ["     ", "     ", "    "],
    ["     ", "     ", "    "],
    ["     ", "     ", "    "],
]


def printTurn(turn):
    global turnCounter
    if turn == 1:
        print(player1Name + "'s Turn")
        block = int(input("Enter Block Number: "))
        if checkMarked(block):
            markBlock(block, "O")
            changeTurn(turn)
            checkWin()
            turnCounter += 1
        else:
            print("Block already marked!!!")
    else:
        print(player2Name + "'s Turn")
        block = int(input("Enter Block Number: "))
        if checkMarked(block):
            markBlock(block, "X")
            changeTurn(turn)
            checkWin()
            turnCounter += 1
        else:
            print("Block already marked!!!")


def checkWin():
    global isNotWin
    if matrix[0][0] == "  O  " and matrix[1][1] == "  O  " and matrix[2][2] == "  O  ":
        print(player1Name + " Win!!!!")
        isNotWin = False
    elif matrix[0][2] == "  X  " and matrix[1][1] == "  X  " and matrix[2][0] == "  X  ":
        print(player2Name + " Win!!!!")
        isNotWin = False
    for x in range(3):

        if matrix[x][0] == "  O  " and matrix[x][1] == "  O  " and matrix[x][2] == "  O  ":
            print(player1Name + " Win!!!!")
            isNotWin = False
            break
        elif matrix[x][0] == "  X  " and matrix[x][1] == "  X  " and matrix[x][2] == "  X  ":
            print(player2Name + " Win!!!!")
            isNotWin = False
            break

        elif matrix[0][x] == "  O  " and matrix[1][x] == "  O  " and matrix[2][x] == "  O  ":
            print(player1Name + " Win!!!!")
            isNotWin = False
            break
        elif matrix[0][x] == "  X  " and matrix[1][x] == "  X  " and matrix[2][x] == "  X  ":
            print(player2Name + " Win!!!!")
            isNotWin = False
            break


def markBlock(blockNumber, sign):

    match blockNumber:
        case 1:
            matrix[-3][-3] = "  " + sign + "  "
        case 2:
            matrix[-3][-2] = "  " + sign + "  "
        case 3:
            matrix[-3][-1] = "  " + sign + "  "
        case 4:
            matrix[-2][-3] = "  " + sign + "  "
        case 5:
            matrix[-2][-2] = "  " + sign + "  "
        case 6:
            matrix[-2][-1] = "  " + sign + "  "
        case 7:
            matrix[-1][-3] = "  " + sign + "  "
        case 8:
            matrix[-1][-2] = "  " + sign + "  "
        case 9:
            matrix[-1][-1] = "  " + sign + "  "


def checkMarked(blockNumber):
    match blockNumber:
        case 1:
            if matrix[0][0] == "     ":
                return True
            return False
        case 2:
            if matrix[0][1] == "     ":
                return True
            return False
        case 3:
            if matrix[0][2] == "     ":
                return True
            return False
        case 4:
            if matrix[1][0] == "     ":
                return True
            return False
        case 5:
            if matrix[1][1] == "     ":
                return True
            return False
        case 6:
            if matrix[1][2] == "     ":
                return True
            return False
        case 7:
            if matrix[2][0] == "     ":
                return True
            return False
        case 8:
            if matrix[2][1] == "     ":
                return True
            return False
        case 9:
            if matrix[2][2] == "     ":
                return True
            return False


def changeTurn(turn):
    if turn == 1:
        global playerTurn
        playerTurn = 2
    else:
        playerTurn = 1


def drawMatrix():
    print(matrix[0][0] + "|" + matrix[0][1] + "|" + matrix[0][2])
    print("-----------------")
    print(matrix[1][0]+"|"+matrix[1][1]+"|"+matrix[1][2])
    print("-----------------")
    print(matrix[2][0]+"|"+matrix[2][1]+"|"+matrix[2][2])


player1Name = input("Enter Player One Name: ")
player2Name = input("Enter Player two Name: ")

drawMatrix()

while turnCounter < maxTurn and isNotWin:
    print("")
    printTurn(playerTurn)
    drawMatrix()
else:
    print("Game is Over")
