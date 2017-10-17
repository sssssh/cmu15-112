# check for list membership: in
a = [2, 3, 5, 2, 6, 2, 2, 7]
print("a      =", a)
print("2 in a =", (2 in a))
print("4 in a =", (4 in a))


# check for list non-membership: not in
print("a      =", a)
print("2 in a =", (2 not in a))
print("4 in a =", (4 not in a))


# count occurrences in list: list.count(item)
print("a          =", a)
print("a.count(1) =", a.count(1))
print("a.count(2) =", a.count(2))
print("a.count(3) =", a.count(3))


# find index of item: list.index(item) list.index(item, start)
print("a            =", a)
print("a.index(6)   =", a.index(6))
print("a.index(2)   =", a.index(2))
print("a.index(2,1) =", a.index(2, 1))
print("a.index(2,4) =", a.index(2, 4))


# problem: crashes when item is not in list
a = [2, 3, 5, 2]
print("a          =", a)
print("a.index(9) =", a.index(9))  # crashes!
print("This line will not run!")


# solution: use (item in list)
print("a =", a)
if (9 in a):
    print("a.index(9) =", a.index(9))
else:
    print("9 not in", a)
print("This line will run now!")
