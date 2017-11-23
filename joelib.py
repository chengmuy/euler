from collections import defaultdict
import itertools as it

def primeFactorize(n):
    """
    Return prime factorization of n

    :param n: number to prime factorize
    :return: dictionary with keys as factors and values as order
    """
    div = 2
    rem = n
    factors = defaultdict(int)
    while rem > 1:
        if rem % div == 0:
            rem /= div
            factors[div] += 1
        else:
            div += 1
    return factors

def isPrime(n):
    """
    Check if n is prime

    :param n: number to check
    :return: True if n is prime, False otherwise
    """

    if n == 0 or n == 1:
        return False

    for div in range(2, int(n**0.5)+1):
        if not n % div:
            return False
    return True

def generatePrimesDivTest():
    for i in it.count(2):
        if isPrime(i):
            yield i

def generatePrimesErat():
    primes = defaultdict(int)

    yield 2
    primes[2] = 4
    yield 3
    primes[3] = 6

    ct = 2

    for i in it.count(4):
        isPrime = True
        for p, val in primes.items():
            if val == i:
                isPrime = False
            if val < i:
                primes[p] += p
        if isPrime:
            primes[i] = i
            yield i


def generatePrimesErat2():
    primes = defaultdict(int)

    yield 2
    primes[2] = 4
    yield 3
    primes[3] = 9

    for i in it.count(5, 2):
        isPrime = True
        for p, val in primes.items():
            if val == i:
                isPrime = False
            if val < i:
                primes[p] += 2*p
        if isPrime:
            primes[i] = i**2
            yield i

def generatePrimesErat3():
    primes = defaultdict(int)
    yield 2
    yield 3
    primes[9] = 3

    for i in it.count(5, 2):
        basePrime = primes.pop(i, None)

        if basePrime: # i is composite
            next = i + 2 * basePrime
            while next in primes:
                next += 2 * basePrime
            primes[next] = basePrime
        else: # i is prime
            yield i
            primes[i**2] = i
