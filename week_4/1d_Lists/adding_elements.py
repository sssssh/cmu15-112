# destructively modifying lists -> in-place
# add an item with list.append(item)
a = [2, 3]
a.append(7)
print(a)


# add a list of items with list += list2
a += [11, 13]
print(a)


# add a list of items with list.extend(list2)
a.extend([110, 120])
print(a)


# insert an item at a given index
a.insert(2, 100000)
print(a)


# non-destructively creating new lists
# add an item with list1 + list2
a = [112, 113]
b = a + [13, 117]
print(a)
print(b)


# insert an item at a given index (with list slices)
b = a[:2] + [5] + a[2:]
print(a)
print(b)


# destructive vs non-destructive
print("Destructive:")
a = [2, 3]
b = a
a += [4]
print(a)
print(b)

print("Non-Destructive:")
a = [2, 3]
b = a
a = a + [4]
print(a)
print(b)
