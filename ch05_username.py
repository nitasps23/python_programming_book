# simple string processing program to generate username

def main():
    print("This program generates computer username.\n")

    # get user's first and last names
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")

    # concat first initial with 7 chars of last name
    uname = first[0] + last[:7]

    # output of username
    print("Your username is:", uname)

main()