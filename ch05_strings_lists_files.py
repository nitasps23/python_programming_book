
str1 = "Hello"
str2 = 'spam'
print(str1, str2)

print(type(str1), type(str2))

# firstName = input("Please enter your name: ")
# print("Hello", firstName)

# interactive indexing
# slicing
greet = "Hello Bob"
print(greet[0], greet[2], greet[4])

x = 8
print(greet[x - 2], greet[-1], greet[-3])

print(greet[0:3], greet[5:9], greet[:5], greet[5:], greet[:])

# concatenation

print("spam" + "eggs", 3 * "spam", (3 * "spam") + ("eggs" * 5))

print(len("spam"))

for i in "spam!":
    print(i, end= " ")

# print abbreviation of month
months = "JanFebMarAprMayJunJulAugSepOctNovDec"

monthAbbrev = months[3:6]
print(monthAbbrev)

# list as sequences
print([1,2] + [3,4])
print([1,2] * 3)

grades = ['A', 'B', 'C', 'D', 'F']
print(grades[0], grades[2:4], len(grades))

myList = [1, 'spam', 4, 'U']
print(myList)

# list is mutable
myList = [34, 26, 15, 10]
print(myList[2])

myList[2] = 0
print(myList)

print(ord('a'), ord('A'), chr(97), chr(90))

# string methods
myString = "Hello, string methods!"
print(myString)
print(myString.split())

print("32,24,25,57".split(","))

# coords = input("Enter the point coordinates (x,y): ").split(",")
# print(coords)
# print(coords[0], coords[1])


# coords = input("Enter the point coordinates (x,y): ").split(",")
# x,y = float(coords[0]), float(coords[1])

# print(x, y, type(x))

print("87 104 97 116".split())

s = "hello, I came here for an argument"
print(s.capitalize())
print(s.title())
print(s.lower())
print(s.upper())
print(s.replace("I", "you"))
print(s.center(30))
print(s.center(50))
print(s.count('e'))
print(s.find(','))
print(" ".join(["Number", "one", "the", "Larch"]))
print("spam".join(["Number", "one", "the", "Larch"]))


# list methods
squares = []
for x in range (1,101):
    squares.append(x*x)

print(squares)


# string formatting
print("Hello {0} {1}, you may have won ${2}".format("Mr.", "Smith", 10000))

print("This int, {0:5}, was placed in a field of width 5".format(7))
print("This int, {0:10}, was placed in a field of width 10".format(7))

print("This float, {0:10.5}, has width 10 and precision 5".format(3.1415926))
print("This float, {0:10.5f}, is fixed at 5 decimal places".format(3.1415926))
print("This float, {0:0.5}, has width 0 and precision 5".format(3.1415926))

print("Compare {0} and {0:0.20}".format(3.14))

print("This is how I want to see float ${0:0.2f}.".format(12000.34444489))


print("left justification: {0:<5}".format("Hi!"))
print("right justification: {0:>5}".format("Hi!"))
print("centered: {0:^5}".format("Hi!"))


# file processing
# multi-line strings
print("Hello\nWorld\n\nGoodbye 32\n")


# file processing
infile = open("ch02_futval.py", "r")
for i in range(5):
    line = infile.read()
    print(line[:])

infile = open("ch02_futval.py", "r")
for line in infile.readlines():
    # process the line here
    infile.close()
    
infile = open("ch02_futval.py", "r")
for line in infile:
    # process the line here
    infile.close()


outfile = open("ch05_username copy.py", "w")