# Static Allocation
a = [[2, 3, 4], [5, 6, 7]]
print(a)


# Dynamic (variable-length) Allocation
# 1 wrong: cannot use * (Shallow Copy)
rows = 3
cols = 2
a = [[0] * cols] * rows  # error: creates shallow copy, creates one unique row, the rest are aliases!
print("This SEEMS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("But see what happens after a[0][0]=42")
print("   a =", a)


# 2 Right: Append Each Row
a=[]
for row in range(rows): a += [[0]*cols]

print("This IS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("   a =", a)


# 2 Even Better: make2dList()
def make2dList(rows, cols):
    a = []
    for row in range(rows):
        a += [[0]*cols]
    return a


a = make2dList(rows, cols)

print("This IS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("   a =", a)


# anoter good option: use a list comprehension
a = [ ([0] * cols) for row in range(rows) ]

print("This IS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("   a =", a)
