# convert temp from C to F
# this version issues cold and heat warnings

def main():
    celsius = float(input("What is the C temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees F.")

    # print warnings for extream temps
    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit < 30:
        print("Brrrr. Be sure to dress warmly!")

main()