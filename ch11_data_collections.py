
# list
print(list(range(10)), "count = ", len(list(range(10))))

print("this is an ex-parrot!".split())

# list operation
lst = [1,2,3,4]

print(3 in lst, 5 in lst)

ans = "Y"
print(ans in "Yy")

print(lst[3])

lst[3] = "hello"
lst[2] = 7
lst[1:3] = ["slice", "assignment"]

print(lst)

# list of identical items
zeros = [0] * 50

print(zeros)

# append - add item to list

nums = []

# x = float(input("Enter a number: "))

# while x >= 0:
#     nums.append(x)
#     print(nums)
#     x = float(input("Enter a number: "))


lst = [1,2,3,4]

print(lst.index(4))

lst.insert(2,88)

print(lst)

new = lst.pop(2)

print(lst, new)

# delete

myList = [34,26,0,10]

del myList[1]
del myList[1:3]

print(myList)

# =======


# dictionary

pw = {"guido": "superprogramer",
      "turing": "gunius",
      "bill": "monopoly"}

print(pw)

print(pw["bill"])

pw["bill"] = "bluescreen"
print(pw["bill"])

pw["newuser"] = "ImANewbie"

print(pw)

# dict operations
print(list(pw.keys()))
print(list(pw.values()))
print(list(pw.items()))
print("bill" in pw, "fred" in  pw)

print(pw.get("bill", "unknown"))
print(pw.get("john", "unknown"))

pw.clear()
print(pw)


# word frequancy

fname = input("")