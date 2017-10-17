# Sieve of Eratosthenes
'''
http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
爱拉托逊斯筛法
是针对自然数列中的自然数而实施的，用于求一定范围内的质数，它的容斥原理之完备性条件是p=H~
'''


def sieve(n):
    isPrime = [True] * (n+1)  # assume all are prime to start
    isPrime[0] = isPrime[1] = False  # except 0 and 1
    primes = []
    for prime in range(n+1):
        if isPrime[prime] == True:
            # we found a prime, so add it to our result
            primes.append(prime)
            # and mark all its multiples as not prime
            for multiple in range(2*prime, n+1, prime):
                isPrime[multiple] = False
    return primes


print(sieve(100))
