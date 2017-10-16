from isPrime import isPrime
from fasterIsPrime import fasterIsPrime
import time


# Verify these are the same
for n in range(100):
    assert(isPrime(n) == fasterIsPrime(n))
print("They seem to work the same!")

# Now let's see if we really sped things up
bigPrime = 499  # Try 1010809, or 10101023, or 102030407
print("Timing isPrime(", bigPrime, ")", end=" ")
time0 = time.time()
print(", returns ", isPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ", (time1-time0) * 1000, "ms")

print("Timing fasterIsPrime(", bigPrime, ")", end=" ")
time0 = time.time()
print(", returns ", fasterIsPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ", (time1-time0) * 1000, "ms")
