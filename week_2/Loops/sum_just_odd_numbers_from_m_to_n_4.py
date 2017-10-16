def sumOfOddsFromMToN(m, n):
    if (m % 2 == 0): m += 1
    return sum(range(m, n+1, 2))


print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))
