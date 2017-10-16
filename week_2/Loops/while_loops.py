# use while loops when there is an indeterminate number of iterations
def leftmostDigit(n):
    n = abs(n)
    while n >= 10:
        n = n // 10
    return n


print(leftmostDigit(72658489290098) == 7)
