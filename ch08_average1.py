
# program to calculate average

def main():
    n = int(input("How many number do you have?"))
    total = 0.0

    for i in range(n):
        x = float(input("Enter a number >> "))
        total = total + x

    print("\nThe average of the numbers is", total / n)


main()