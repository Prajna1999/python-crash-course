import graphics


def main():
    win = graphics.GraphWin('Face', 200, 150)  # give title and dimensions
    win.yUp()  # make right side up coordinates!

    head = graphics.Circle(Point(40, 100), 25)  # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = graphics.Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = graphics.Line(
        Point(45, 105), graphics.Point(55, 105))  # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = graphics.Oval(Point(30, 90), Point(
        50, 85))  # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    label = Text(Point(100, 120), 'A face')
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()


main()
