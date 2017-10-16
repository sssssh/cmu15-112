def sumFromMToN(m, n):
    return sum(range(m, n+1))


print(sumFromMToN(5, 10) == 5+6+7+8+9+10)



# other way
def sumToN(n):
    # helper function
    return n * (n + 1) // 2


def sumFromMToN_byFormula(m, n):
    return sumToN(n) - sumToN(m-1)


print(sumFromMToN_byFormula(5, 10) == 5+6+7+8+9+10)
