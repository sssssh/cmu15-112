def sumOfOddsFromMToN(m, n):
    total = 0
    for x in range(m, n+1):
        if x % 2 == 1:
            total += x
    return total


print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5, 9) == (5+7+9))
