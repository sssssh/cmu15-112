# This is a common early mistake (confusing print and return):
def cubed(x):
    print(x ** 3)  # Here is the error!


cubed(2)  # seems to work!
print(cubed(3))  # sort of works (but prints None, which is weird)
print(2 * cubed(4))  # Error!


def cubed(x):
    return (x ** 3)


cubed(4)  # noting (seems to be ignored why?)
print(cubed(2))  # works 8
print(2 * cubed(4))  # works!
