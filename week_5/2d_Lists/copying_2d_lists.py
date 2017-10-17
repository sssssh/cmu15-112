import copy


# wrong: cannot use copy.copy (shallow copy)
# Create a 2d list
a = [[1, 2, 3], [4, 5, 6]]

# Try to copy it
b = copy.copy(a)  # Error:  creates shallow copy

# At first, things seem ok
print("At first...")
print("   a =", a)
print("   b =", b)

# Now modify a[0][0]
a[0][0] = 9
print("But after a[0][0] = 9")
print("   a =", a)
print("   b =", b)


# Right:use copy.deepcopy
# Try to copy it
b = copy.deepcopy(a)  # Correct!

# At first, things seem ok
print("At first...")
print("   a =", a)
print("   b =", b)

# Now modify a[0][0]
a[0][0] = 9
print("And after a[0][0] = 9")
print("   a =", a)
print("   b =", b)


# limitations of copy.deepcopy
a = [[0]*2]*3 # makes 3 shallow copies of (aliases of) the same row
a[0][0] = 42  # appears to modify all 3 rows
print(a)      # prints [[42, 0], [42, 0], [42, 0]]

# now do it again with a deepcopy


a = [[0]*2]*3  # makes 3 shallow copies of the same row
a = copy.deepcopy(a)  # meant to make each row distinct
a[0][0] = 42  # so we hope this only modifies first row
print(a)  # STILL prints [[42, 0], [42, 0], [42, 0]]

# now one more time with a simple deepcopy alternative that does
# what we thought deepcopy did...


def myDeepCopy(a):
    if (isinstance(a, list) or isinstance(a, tuple)):
        return [myDeepCopy(element) for element in a]
    else:
        return copy.copy(a)

a = [[0]*2]*3  # makes 3 shallow copies of the same row
a = myDeepCopy(a)  # once again, meant to make each row distinct
a[0][0] = 42  # so we hope this only modifies first row
print(a)  # finally, prints [[42, 0], [0, 0], [0, 0]]

# what's going on with deepcopy? Answer: if the original list has aliases,
# the deepcopied list will have aliases (of a single copy, not the original).
# So copy.deepcopy preserves alias structure!
