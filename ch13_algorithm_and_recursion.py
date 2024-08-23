
# searching

def search(x, nums):
    # nums is a list of numbers and x is a number
    # returns the position in the list where x occurs or -1 if
    #       x is not in the list
    # if x in nums:
        # do something
    
    try:
        return nums.index(x)
    except:
        return -1

print(search(0, [3,1,4,2,5]))


# linear search
def search_lin(x, nums):
    for i in range(len(nums)):
        if nums[i] == x:       # item found, return the index value
            return i
    return -1   # loop finished, item was not in list

print(search_lin(2, [3,1,4,2,5,2]))

# binary search

def search(x, nums):
    low = 0
    high = len(nums) - 1
    while low <= high:          # there's still range to search
        mid = (low + high) // 2 # position of middle item
        item = nums[mid]
        if x == item:           # found it! return the index
            return mid
        elif x < item:          # x is in lower half of range
            high = mid - 1      #   move top marker down
        else:                   # x is in upper half
            low = mid + 1       #   move bottom marker up
    return -1                   # no range left to search
                                # x is not there

print(search_lin(5, [3,1,4,2,5,2]))

# recursive function
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(3))

# string reversal

def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
    

print(reverse("hello"))


# anagrams

def anagrams(s):
    # returns a list of all anagrams of string s
    if s == "":
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])
        return ans
    

print(anagrams("hello"))


