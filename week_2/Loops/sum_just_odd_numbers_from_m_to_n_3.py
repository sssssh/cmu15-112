# Here we will range in reverse (not wise in this case, but instructional)


def sumOfOddsFromMToN(m, n):
    if (n % 2 == 0):
        # n is even, subtract 1 to start on an odd
        n -= 1
    total = 0
    for x in range(n, m-1, -2):  # be careful here!
        total += x
    return total


print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5, 9) == (5+7+9))
