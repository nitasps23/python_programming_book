# convert temp from C to F

def main():
    celsius = eval(input("What is the C temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees F.")

main()