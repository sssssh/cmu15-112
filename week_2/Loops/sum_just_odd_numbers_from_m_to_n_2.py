def sumOfOddsFromMToN(m, n):
    if (m % 2 == 0):
        # m is even, add 1 to start on an odd
        m += 1
    total = 0
    for x in range(m, n+1, 2):
        total += x
    return total

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))
