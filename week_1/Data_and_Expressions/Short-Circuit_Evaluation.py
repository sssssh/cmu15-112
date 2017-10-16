def yes():
    return True


def no():
    return False


def crash():
    return 1/0  # crashes!


print(no() and crash())
print(crash() and no())
print(yes() and crash())


print(yes() or crash())
print(crash() or yes())
print(no() or crash())


def isPositive(n):
    result = (n > 0)
    print("isPositive(",n,") =", result)
    return result


def isEven(n):
    result = (n % 2 == 0)
    print("isEven(",n,") =", result)
    return result


print("Test 1: isEven(-4) and isPositive(-4))")
print(isEven(-4) and isPositive(-4)) # Calls both functions
print("----------")
print("Test 2: isEven(-3) and isPositive(-3)")
print(isEven(-3) and isPositive(-3)) # Calls only one function!
