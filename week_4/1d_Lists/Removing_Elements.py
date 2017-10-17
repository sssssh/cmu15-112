# in-place
# Remove an item with list.remove(item)
a = [2, 3, 5, 3, 7, 6, 5, 11, 13]
print("a =", a)

a.remove(5)
print("After a.remove(5), a=", a)

a.remove(5)
print("After another a.remove(5), a=", a)


# Remove an item at a given index with list.pop(index)
print("a=", a)
item = a.pop(3)
print("After item = a.pop(3)")
print("   item =", item)
print("   a =", a)

item = a.pop(3)
print("After another item = a.pop(3)")
print("   item =", item)
print("   a =", a)

# Remove last item with list.pop()
item = a.pop()
print("After item = a.pop()")
print("   item =", item)
print("   a =", a)


# Remove an item with slice assignment
a = [2, 3, 4, 5, 6, 7, 8]
a[2:4] = []
print("a =", a)


# Remove an item with the del operator
a = [2, 3, 4, 5, 6, 7, 8]
del a[2:4]
print("a =", a)


# creating new lists
# Remove an item at a given index with list slices
a = [2, 3, 5, 3, 7, 5, 11, 13]
print("a =", a)

b = a[:2] + a[3:]
print("After b = a[:2] + a[3:]")
print("   a =", a)
print("   b =", b)
