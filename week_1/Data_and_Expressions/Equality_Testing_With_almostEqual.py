print("The problem....")
d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)  # False never use == with floats!


print()
print("The solution...")
epsilon = 10**-10
print(abs(d2 - d1) < epsilon)  # True!


print()
print("Once again, using a useful helper function, almostEqual:")


def almostEqual(d1, d2):
    epsilon = 10**-10
    return (abs(d2 - d1) < epsilon)


d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)  # still False
print(almostEqual(d1, d2))  # True, and now packaged in a handy reusable functions!
