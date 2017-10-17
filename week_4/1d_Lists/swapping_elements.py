# failed swap
a = [2, 3, 5, 7]
print("a =", a)


a[0] = a[1]
a[1] = a[0]
print("After failed swap of a[0] and a[1]:")
print("    a=", a)


# swap with a temp variable
a = [2, 3, 5, 7]
print("a =", a)


temp = a[0]
a[0] = a[1]
a[1] = temp
print("After swapping a[0] and a[1]:")
print("    a=", a)


# swap with parallel (tuple) assignment
a = [2, 3, 5, 7]
print("a =", a)

a[0], a[1] = a[1], a[0]
print("After swapping a[0] and a[1]:")
print("   a=", a)
