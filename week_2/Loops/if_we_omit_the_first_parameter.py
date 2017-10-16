def sumToN(n):
    total = 0
    for x in range(n+1):
        total += x
    return total


print(sumToN(5) == 0+1+2+3+4+5)
