
"""projectile.py
provides a simple class for modeling the 
flight of projectiles."""

import math

class Projectile:

    """simulates the flight of simple projectiles near the earth's
    surface, ignoring wide resistance. Tracking is done in two
    dimentions, height (y) and distance (x)."""

    def __init__(self, angle, velocity, height):
        """create a projectile with given launch angle, initial
        velocity and height"""
        self.xpos = 0.0
        self.ypos = height
        theta = math.radians(angle)
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)

    def update(self, time):
        """update the state of this projectile to move it time seconds
        farther into its flight"""
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1) /2.0
        self.yvel = yvel1

    def getX(self):
        "returns the x position (distance) of this projectile."
        return self.xpos
    
    def getY(self):
        "returns the y position (height) of this projectile."
        return self.ypos
    
