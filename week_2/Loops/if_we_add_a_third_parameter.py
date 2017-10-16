def sumEveryKthFromMToN(m, n, k):
    total = 0
    for x in range(m, n+1, k):
        total += x
    return total


print(sumEveryKthFromMToN(5, 20, 7) == (5 + 12 + 19))
