def happy():
    print("Happy birthday to you!")

def sing(person):
    happy()
    happy()
    print("Happy birthday, dear", person + ".")
    happy()

def main():
    sing("Nita")
    print()
    sing("Laura")
    print()
    sing("Mom")

main()