from tkinter import Tk, Canvas


def draw(canvas, width, height):
    margin = 10
    # Approach #1: Add margin to top/left, subtract margin from bottom/right:
    canvas.create_rectangle(margin, margin, width-margin, height-margin,
                            fill="darkGreen")
    # Approach #2: add/subtract width/height from center (cx, cy)
    (cx, cy) = (width/2, height/2)
    (rectWidth, rectHeight) = (width/4, height/4)
    canvas.create_rectangle(cx - rectWidth/2, cy - rectHeight/2,
                            cx + rectWidth/2, cy + rectHeight/2,
                            fill="orange")


def runDrawing(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")


runDrawing(400, 200)
