
import math

def main():
    angle = float(input("Enter the launch angle (in degree): "))
    vel = float(input("Enter the initial velocity (in meters/sec): "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position calculation: "))

    # convert angle to radians
    theta = math.radians(angle)

    # set the initial position and velocities in x and y directions
    xpos = 0
    ypos = h0
    xvel = vel * math.cos(theta)
    yvel = vel * math.sin(theta)

    # loop until the ball hits the ground
    while ypos >= 0.0:
        # calculate position and velocity in time seconds
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1) / 2.0
        yvel = yvel1

    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

main()