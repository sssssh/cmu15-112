# This is the worst way so far -- too confusing.
def sumOfOddsFromMToN(m, n):
    return sum(range(m + (1 - m % 2), n+1, 2))  # this works, but it's gross!


print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5, 9) == (5+7+9))
