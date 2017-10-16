# Note: there are faster/better ways.  We're just going for clarity and simplicity here.
def isPrime(n):
    if (n < 2):
        return False
    for factor in range(2, n):
        if (n % factor == 0):
            return False
    return True


# And take it for a spin
for n in range(100):
    if isPrime(n):
        print(n, end=" ")


print()
