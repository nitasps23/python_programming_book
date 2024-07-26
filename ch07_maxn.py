# find the max of a series of numbers

def main():
    n = int(input("How many numbers are there? "))

    # set max to be the first value
    maxval = float(input("Enter a number >> "))

    # compare the n-1 seccessive values
    for i in range(n-1):
        x = float(input("Enter a number >> "))
        if x > maxval:
            maxval = x
    
    print("The largest value is", maxval)

main()