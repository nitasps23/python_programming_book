# class definition for an n-sided die

from random import randrange

class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1,self.sides+1)

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value


def main():
    die1 = MSDie(12)
    die1.setValue(8)
    print(die1.getValue())

main()

die1 = MSDie(13)
print(die1.getValue())

die1.setValue(8)
print(die1.getValue())