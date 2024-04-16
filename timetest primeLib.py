import primeLib as p
from time import time


def timeMiller(prime,N):
    start = time()

def timeSieve(a,b,N):
    start = time()
    p.primeSieve(a,b)
    print(time()-start)


def timeNext(prime,N):
    """Returns elapsed time when performing N steps with function nextPrime()"""
    start = time.time()
    curr = prime
    for i in range(N):
        curr = p.nextPrime(curr)
    print(time.time()-start)


def timePrev(prime,N):
    """Returns elapsed time when performing N steps with function prevPrime()"""
    start = time.time()
    curr = prime
    for i in range(N):
        curr = p.prevPrime(curr)
    print(time.time()-start)

