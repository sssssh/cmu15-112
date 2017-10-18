# snake-demo.py

# Note: there is a snake tutorial from previous semesters here:
#    http://www.kosbie.net/cmu/fall-11/15-112/handouts/snake/snake.html
# But this is different in two key ways:
#    1) This uses this semester's framework (run function, and in Python3)
#    2) This uses a list of tuples to represent the snake
# You should understand both solutions, and be able to adapt that
# tutorial to use this semester's framework.

from tkinter import Tk, Canvas, ALL
import random


def init(data):
    data.rows = 10
    data.cols = 10
    data.margin = 5  # margin around grid
    data.snake = [(data.rows/2, data.cols/2)]
    data.direction = (0, +1)  # (drow, dcol)
    placeFood(data)
    data.timerDelay = 250
    data.gameOver = False
    data.paused = True


# getCellBounds from grid-demo.py
def getCellBounds(row, col, data):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth = data.width - 2*data.margin
    gridHeight = data.height - 2*data.margin
    x0 = data.margin + gridWidth * col / data.cols
    x1 = data.margin + gridWidth * (col+1) / data.cols
    y0 = data.margin + gridHeight * row / data.rows
    y1 = data.margin + gridHeight * (row+1) / data.rows
    return (x0, y0, x1, y1)


def mousePressed(event, data):
    data.paused = False


def keyPressed(event, data):
    if (event.keysym == "p"):
        data.paused = True
        return
    elif (event.keysym == "r"):
        init(data)
        return
    if (data.paused or data.gameOver):
        return
    if (event.keysym == "Up"):
        data.direction = (-1, 0)
    elif (event.keysym == "Down"):
        data.direction = (+1, 0)
    elif (event.keysym == "Left"):
        data.direction = (0, -1)
    elif (event.keysym == "Right"):
        data.direction = (0, +1)
    # for debugging, take one step on any keypress
    takeStep(data)


def timerFired(data):
    if (data.paused or data.gameOver): return
    takeStep(data)


def takeStep(data):
    (drow, dcol) = data.direction
    (headRow, headCol) = data.snake[0]
    (newRow, newCol) = (headRow+drow, headCol+dcol)
    if ((newRow < 0) or (newRow >= data.rows) or
        (newCol < 0) or (newCol >= data.cols) or
       ((newRow, newCol) in data.snake)):
        data.gameOver = True
    else:
        data.snake.insert(0, (newRow, newCol))
        if (data.foodPosition == (newRow, newCol)):
            placeFood(data)
        else:
            # didn't eat, so remove old tail (slither forward)
            data.snake.pop()


def placeFood(data):
    data.foodPosition = None
    row0 = random.randint(0, data.rows-1)
    col0 = random.randint(0, data.cols-1)
    for drow in range(data.rows):
        for dcol in range(data.cols):
            row = (row0 + drow) % data.rows
            col = (col0 + dcol) % data.cols
            if (row, col) not in data.snake:
                data.foodPosition = (row, col)
                return


def drawBoard(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            (x0, y0, x1, y1) = getCellBounds(row, col, data)
            canvas.create_rectangle(x0, y0, x1, y1, fill="white")


def drawSnake(canvas, data):
    for (row, col) in data.snake:
        (x0, y0, x1, y1) = getCellBounds(row, col, data)
        canvas.create_oval(x0, y0, x1, y1, fill="blue")


def drawFood(canvas, data):
    if (data.foodPosition != None):
        (row, col) = data.foodPosition
        (x0, y0, x1, y1) = getCellBounds(row, col, data)
        canvas.create_oval(x0, y0, x1, y1, fill="green")


def drawGameOver(canvas, data):
    if (data.gameOver):
        canvas.create_text(data.width/2, data.height/2, text="Game over!",
                           font="Arial 26 bold")


def redrawAll(canvas, data):
    drawBoard(canvas, data)
    drawSnake(canvas, data)
    drawFood(canvas, data)
    drawGameOver(canvas, data)


# use the run function as-is
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init

    class Struct(object):
        pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100  # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
              mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
              keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


run(300, 300)
