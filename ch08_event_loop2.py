
# keyboard driven color changing window

from graphics import *

def handleKey(k, win):
        # process the key
        if k == "r":
            win.setBackground("pink")
        elif k == "w":
            win.setBackground("white")
        elif k == "g":
            win.setBackground("lightgray")
        elif k == "b":
            win.setBackground("lightblue")


def handleClick(pt, win):
    # create an entry to type
    entry = Entry(pt, 10)
    entry.draw(win)

    # go modal: loop until user click enter key
    while True:
        key = win.getKey()
        if key == "Return": break

    # undraw the entry and create and draw text
    entry.undraw()
    typed = entry.getText()
    Text(pt, typed).draw(win)

    # clear (ignore) mouse click during text entry
    win.checkMouse

def main():
    win = GraphWin("Click and Type", 500, 500)

    # event loop: handle key press and mouse click until user presses 'q' key
    while True:
        key = win.checkKey()
        if key == "q":  # exit
            break

        if key:
            handleKey(key, win)

        pt = win.checkMouse()
        if pt:
            handleClick(pt, win)

    win.close()


main()

        
