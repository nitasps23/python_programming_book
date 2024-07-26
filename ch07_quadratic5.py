# a program that computes the real roots of a quadratic equation
# illustrates use of the math library
# note: this program crashes if the equation has no real roots
# with exception handling to catch errors

import math  # make the math library available

def main():
    print("This program finds the real solutions to a quadratic\n")

    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2)
    except ValueError as exc0bj:
        if str(exc0bj) == "math domain error":
            print("No real roots")
        else:
            print("Invalid coefficient given")
    except:
        print("\nSomething went wrong, sorry!")

main()