def hypotenuse(a, b):
    return ((a ** 2) + (b ** 2)) ** 0.5


print(hypotenuse(3, 4))
print("--------------------")


def xor(b1, b2):
    return ((b1 and (not b2)) or (b2 and (not b1)))


print(xor(True, True))
print(xor(True, False))
print(xor(False, True))
print(xor(False, False))
print("---------------------")


def isPositive(n):
    return (n > 0)


print(isPositive(10))
print(isPositive(-1.234))
