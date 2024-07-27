
def main():
    total = 0.0
    count = 0
    moredata = "yes"

    while moredata[0] == "y":
        x = float(input("Enter a number >> "))
        total = total + x
        count = count + 1
        moredata = input("Do you have more number (yes/no)? ")
    print("\nThe average of the numbers is", total / count)


main()