
# import graphics

# win = graphics.GraphWin()

from graphics import *

# def main():
#     win = GraphWin("My Circle", 100, 100)
#     c = Circle(Point(50,50), 10)
#     c.draw(win)
#     win.getMouse() # Pause to view result
#     win.close()    # Close window when done

# main()

# ============

# p = Point(50, 60)
# p.getX()
# p.getY()
# win = GraphWin()
# p.draw(win)
# p2 = Point(140, 100)
# p2.draw(win)

# win.getMouse() # Pause to view result
# win.close()    # Close window when done

# ==========

# # open graphics window
# win = GraphWin('Shapes')

# # draw a red circle centered at point (100,100) with radius 30
# center = Point(100, 100)
# circ = Circle(center, 30)
# circ.setFill('red')
# circ.draw(win)

# # put text label in the center of circle
# label = Text(center, "Red Circle")
# label.draw(win)

# # draw a square using a rectangle object
# rect = Rectangle(Point(30,30), Point(70,70))
# rect.draw(win)

# # draw a line segment using a line object
# line = Line(Point(20,30), Point(180, 165))
# line.draw(win)

# # Draw an oval using oval object
# oval = Oval(Point(20,150), Point(180,199))
# oval.draw(win)

# win.getMouse() # Pause to view result
# win.close()    # Close window when done

# =======

# correct way to create a separate circle for each eye, using clone

# leftEye = Circle(Point(80, 50), 5)
# leftEye.setFill('yellow')
# leftEye.setOutline('red')
# rightEye = leftEye.clone()
# rightEye.move(20,0)

# ========

# choosing coordinates
# create a default 200x200 window
win = GraphWin("Tic-Tac-Toe")

# set coordinates to go from (0,0) in the lower left
# to (3,3) in the upper right
win.setCoords(0.0, 0.0, 3.0, 3.0)

# draw vertical lines
Line(Point(1,0), Point(1,3)).draw(win)
Line(Point(2,0), Point(2,3)).draw(win)

# draw horizontal lines
Line(Point(0,1), Point(3,1)).draw(win)
Line(Point(0,2), Point(3,2)).draw(win)

win.getMouse()

# ============

