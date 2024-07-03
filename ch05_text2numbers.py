# a program to convert a text message into sequence of numbers
# using Unicode encoding

def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message. \n")

    # get the message to encode
    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes: ")

    # Loop through the message and print out the Unicode values
    for ch in message:
        print(ord(ch), end=" ")

    print() # blank line before prompt

main()