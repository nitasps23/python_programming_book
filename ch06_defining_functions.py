
def main():
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday, dear Fred.")
    print("Happy birthday to you!")

main()

print()

def happy():
    print("Happy birthday to you!")

happy()

print()

def singFred():
    happy()
    happy()
    print("Happy birthday, dear Fred.")
    happy()

singFred()

print()

def singLucy():
    happy()
    happy()
    print("Happy birthday, dear Lucy.")
    happy()

singLucy()

print()

def main():
    singFred()
    print()
    singLucy()

main()

print()

def sing(person):
    happy()
    happy()
    print("Happy birthday, dear", person + ".")
    happy()

sing("Nita")
print()
sing("Laura")

print()

def main():
    sing("Nita")
    print()
    sing("Laura")
    print()
    sing("Mom")

main()


# function that returns values
def square(x):
    return x ** 2

print(square(5) + 100)
print(square(5))

x = 4
y = square(x)
print(y)


import math

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p1.getY()))
    return dist


# return more values
def sumDiff(x,y):
    sum = x + y
    diff = x - y
    return sum, diff

num1, num2 = input("Please enter two numbers (num1, num2) ").split(",")
s, d = sumDiff(float(num1), float(num2))
print("The sum is", s, "and the difference is", d)

