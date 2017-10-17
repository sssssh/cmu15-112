import copy


# Copy vs Alias
# Create a list
a = [2, 3]


# Try to copy it
b = a  # Error! Not a copy, but an alias
c = copy.copy(a)  # Ok


# At first, things seem ok
print("At first...")
print("   a =", a)
print("   b =", b)
print("   c =", c)


# Now modify a[0]
a[0] = 42
print("But after a[0] = 42")
print("   a =", a)
print("   b =", b)
print("   c =", c)
