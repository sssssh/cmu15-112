from tkinter import Tk, Canvas


def draw(canvas, width, height):
    pass # replace with your drawing code!


def runDrawing(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")


runDrawing(400, 200)
