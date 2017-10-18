from tkinter import Tk, NW, ALL, Canvas, PhotoImage


def init(data):
    data.step = 0
    loadPlayingCardImages(data)  # always load images in init!


def loadPlayingCardImages(data):
    cards = 55  # cards 1-52, back, joker1, joker2
    data.cardImages = []
    for card in range(cards):
        rank = (card % 13)+1
        suit = "cdhsx"[card//13]
        filename = "playing-card-gifs/%s%d.gif" % (suit, rank)
        data.cardImages.append(PhotoImage(file=filename))


def getPlayingCardImage(data, rank, suitName):
    suitName = suitName[0].lower()  # only car about first letter
    suitNames = "cdhsx"
    assert(1 <= rank <= 13)
    assert(suitName in suitNames)
    suit = suitNames.index(suitName)
    return data.cardImages[13*suit + rank - 1]


def getSpecialPlayingCardImage(data, name):
    specialNames = ["back", "joker1", "joker2"]
    return getPlayingCardImage(data, specialNames.index(name)+1, "x")


def mousePressed(event, data):
    pass


def keyPressed(event, data):
    pass


def timerFired(data):
    data.step += 1


def redrawAll(canvas, data):
    suitNames = ["Clubs", "Diamonds", "Hearts", "Spades", "Xtras"]
    suit = (data.step//10) % len(suitNames)
    suitName = suitNames[suit]
    cards = 3 if (suitName == "Xtras") else 13
    margin = 10
    (left, top) = (margin, 40)
    for rank in range(1, cards+1):
        image = getPlayingCardImage(data, rank, suitName)
        if (left + image.width() > data.width):
            (left, top) = (margin, top + image.height() + margin)
        canvas.create_image(left, top, anchor=NW, image=image)
        left += image.width() + margin
    canvas.create_text(data.width/2, 20, text=suitName, font="Arial 28 bold")


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
    # Create root before calling init (so we can create images in init)
    root = Tk()
    # Set up data and call init

    class Struct(object):
        pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 250  # milliseconds
    init(data)
    # create the root and the canvas
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


run(420, 360)
