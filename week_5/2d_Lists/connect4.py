# connect4.py

# A simple game of connect4 with a text interface
# based on the wordSearch code written in class.

def playConnect4():
    rows = 6
    cols = 7
    board = makeBoard(rows, cols)
    player = "X"
    moveCount = 0
    printBoard(board)
    while (moveCount < rows*cols):
        moveCol = getMoveCol(board, player)
        moveRow = getMoveRow(board, moveCol)
        board[moveRow][moveCol] = player
        printBoard(board)
        if checkForWin(board, player):
            print("*** Player %s Wins!!! ***" % player)
            return
        moveCount += 1
        player = "O" if (player == "X") else "X"
    print("*** Tie Game!!! ***")

def makeBoard(rows, cols):
    return [ (["-"] * cols) for row in range(rows) ]

def printBoard(board):
    rows = len(board)
    cols = len(board[0])
    print()
    # first print the column headers
    print("    ", end="")
    for col in range(cols):
        print(str(col+1).center(3), " ", end="")
    print()
    # now print the board
    for row in range(rows):
        print("    ", end="")
        for col in range(cols):
            print(board[row][col].center(3), " ", end="")
        print()

def getMoveCol(board, player):
    cols = len(board[0])
    while True:
        response = input("Enter player %s's move (column number) --> " %
                         (player))
        try:
            moveCol = int(response)-1  # -1 since user sees cols starting at 1
            if ((moveCol < 0) or (moveCol >= cols)):
                print("Columns must be between 1 and %d. " % (cols), end="")
            elif (board[0][moveCol] != "-"):
                print("That column is full! ", end="")
            else:
                return moveCol
        except:
            # they did not even enter an integer!
            print("Columns must be integer values! ", end="")
        print("Please try again.")

def getMoveRow(board, moveCol):
    # find first open row from bottom
    rows = len(board)
    for moveRow in range(rows-1, -1, -1):
        if (board[moveRow][moveCol] == "-"):
            return moveRow
    # should never get here!
    assert(False)

def checkForWin(board, player):
    winningWord = player * 4
    return (wordSearch(board, winningWord) != None) # that was easy!

##############################################
# taken from wordSearch.py
##############################################

def wordSearch(board, word):
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            result = wordSearchFromCell(board, word, row, col)
            if (result != None):
                return result
    return None

def wordSearchFromCell(board, word, startRow, startCol):
    for drow in [-1, 0, +1]:
        for dcol in [-1, 0, +1]:
            if ((drow != 0) or (dcol != 0)):
                result = wordSearchFromCellInDirection(board, word,
                                                       startRow, startCol,
                                                       drow, dcol)
                if (result != None):
                    return result
    return None

def wordSearchFromCellInDirection(board, word, startRow, startCol, drow, dcol):
    (rows, cols) = (len(board), len(board[0]))
    dirNames = [ ["up-left"  ,   "up", "up-right"],
                 ["left"     ,   ""  , "right"   ],
                 ["down-left", "down", "down-right" ] ]
    for i in range(len(word)):
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or
            (col < 0) or (col >= cols) or
            (board[row][col] != word[i])):
            return None
    return (word, (startRow, startCol), dirNames[drow+1][dcol+1])

playConnect4()
