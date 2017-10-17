# example
# Create a list
a = [2, 3, 5, 7]

# Create an alias to the list
b = a

# We now have two references (aliases) to the SAME list
a[0] = 42
b[1] = 99
print(a)
print(b)


# function parameters are aliases
def f(a):
    a[0] = 42


a = [2, 3, 5, 7]
f(a)
print(a)


# anoter example
# Create a list
a = [2, 3, 5, 7]

# Create an alias to the list
b = a

# Create a different list with the same elements
c = [2, 3, 5, 7]

# a and b are references (aliases) to the SAME list
# c is a reference to a different but EQUAL list

print("initially:")
print("  a==b  :", a == b)
print("  a==c  :", a == c)
print("  a is b:", a is b)
print("  a is c:", a is c)

# Now changes to a also change b (the SAME list) but not c (a different list)
a[0] = 42
print("After changing a[0] to 42")
print("  a=", a)
print("  b=", b)
print("  c=", c)
print("  a==b  :", a == b)
print("  a==c  :", a == c)
print("  a is b:", a is b)
print("  a is c:", a is c)
