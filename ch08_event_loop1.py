
# keyboard driven color changing window

from graphics import *

def main():
    win = GraphWin("Color Window", 500, 500)

    # event loop: handle key press until user presses 'q' key
    while True:
        key = win.getKey()
        if key == "q":  # exit
            break

        # process the key
        if key == "r":
            win.setBackground("pink")
        elif key == "w":
            win.setBackground("white")
        elif key == "g":
            win.setBackground("lightgray")
        elif key == "b":
            win.setBackground("lightblue")

    # exit
    win.close()

main()