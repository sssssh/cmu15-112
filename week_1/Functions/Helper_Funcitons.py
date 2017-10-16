def onesDigit(n):
    return n % 10


def largerOnesDigit(x, y):
    return max(onesDigit(x), onesDigit(y))


print(largerOnesDigit(134, 673))
print(largerOnesDigit(132, 674))
