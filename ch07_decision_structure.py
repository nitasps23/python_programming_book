# simple condition

print(3 < 4, 3 * 4 < 3 + 4, "Hello" == "hello")

# conditional program execution
import math
print(math.__name__)

print(__name__)


# if __name__ == '__main__':
#     main()


# two-way decisions

# multi-way decisions


# study in design - max of three
def main():
    x1, x2, x3 = eval(input("Please enter three values: "))

    maxval = max(x1,x2,x3)

    # missing code set maxval to the value of the largest

    print("The largest value is", maxval)

main()