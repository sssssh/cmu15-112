# Note: this is still not the fastest way, but it's a nice improvement.
def fasterIsPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3, maxFactor+1, 2):
        if (n % factor == 0):
            return False
    return True


# And try out this version:
for n in range(100):
    if fasterIsPrime(n):
        print(n, end=" ")


print()
