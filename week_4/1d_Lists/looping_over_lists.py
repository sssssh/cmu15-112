# looping with: for item in list
a = [2, 3, 5, 7]
print("Here are the items in a:")
for item in a:
    print(item)


# looping with: for index in range(len(list))
print("Here are the items in a with their indexes:")
for index in range(len(a)):
    print("a[", index, "] =", a[index])


# looping backward
print("And here are the items in reverse:")
for index in range(len(a)):
    revIndex = len(a)-1-index
    print("a[", revIndex, "] =", a[revIndex])


# looping backward with reversed(list)
print("And here are the items in reverse:")
for item in reversed(a):
    print(item)
print(a)


# looping backward with destructive list.reverse()
print("And here are the items in reverse:")
a.reverse()
for item in a:
    print(item)
print(a)


# hazard: modifying while looping
a = [2, 3, 5, 3, 7]
print("a =", a)

# Failed attempt to remove all the 3's
for index in range(len(a)):
    if (a[index] == 3):  # this eventually crashes!
        a.pop(index)

print("This line will not run!")
