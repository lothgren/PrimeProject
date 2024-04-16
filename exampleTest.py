from primeLib import primeSieve, nextPrime



def example():
    """Generates all primes in the interval [10000,10050] then adds
    the next occuring prime larger then 10050"""

    l = primeSieve(10000,10050)
    new = nextPrime(l[-1])
    l.append(new)

    print(*l) #output: 10007 10009 10037 10039 10061

example()

