def sumFromMtoN(m, n):
    total = 0
    # note that range(x, y) includes x but excludes y
    for x in range(m, n+1):
        total += x
    return total


print(sumFromMtoN(5, 10) == 5 + 6 + 7 + 8 + 9 + 10)
