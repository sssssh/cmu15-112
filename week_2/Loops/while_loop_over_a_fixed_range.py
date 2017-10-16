def sumToN(n):
    total = 0
    counter = 1
    while counter <= n:
        total += counter
        counter += 1
    return total


def sum_To_N(n):
    total = 0
    for num in range(n+1):
        total += num
    return total


print(sumToN(5) == sum_To_N(5) == 1+2+3+4+5)


def buggySumToN(n):
    # note: this not only uses a "while" instead of a "for" loop,
    # but it also contains a bug. Ugh.
    total = 0
    counter = 0
    while (counter <= n):
        counter += 1
        total += counter  # bug is here!
    return total


print(buggySumToN(5) == 1+2+3+4+5)
