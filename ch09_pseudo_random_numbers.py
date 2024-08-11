 # randrange

from random import randrange

print(randrange(1,6))

# random

from random import random

print(random())

# test
def gameOver(a,b):
    # a and b represent scores for a racquetball game
    # returns True if the game is over, False otherwise
    return a == 15 or b == 15

print(gameOver(0,0))
print(gameOver(5,10))
print(gameOver(15,3))

def simOneGame(probA, probB):
    # simulate a single game between players
    # return final scores for A and B
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

print(simOneGame(.5,.5))
print(simOneGame(.3,.3))
print(simOneGame(.9,.4))
print(simOneGame(.4,.6))


# prototyping

from random import random

def simOneGame():
    scoreA = 0
    scoreB = 0
    serving = "A"

    for i in range(30):
        if serving == "A":
            if random() < .5:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < .5:
                scoreB = scoreB + 1
            else:
                serving = "A"
    print(scoreA, scoreB)

if __name__ =='__main__': simOneGame()