# Package primeLib provides standard functions for operating on prime number
# 
# Prime numbers are tied to many different theorems which can be used to
# time-efficintly run primality test and generate new primes. 
# 
# PrimeLib perform primality test with a complexety of O(sqrt(n)) or with 
# a minimal loss of accuarcy O(log(n)^3). It also efficiently return a 
# list of prime number from intervals less than 10^7. For higher primes 
# it can still easily calculate the next/previous prime from a given number 
# considerably higher.
#



from random import randint

def isPrime(n: int):
    """Checks if input n is a prime number"""
    #T(n) = O(sqrt(n))
    
    if n == 2 or n == 3:
        return True
    if n <= 1 or n%2 == 0 or n%3 == 0:
        return False
    
    i = 5
    while i*i <= n:
        if n % i == 0 or n%(i+2) == 0:
            return False
        i += 6
    
    return True


def __modulo(a,d,n):
    """Returns the modulo (a^d)%n with less chance of overflow"""
    result = 1

    a = a%n
    while d > 0:
        if d%2 != 0:
            result = (result*a)%n
        
        d = d//2
        a = a**2%n

    return result


def millerRabin(n:int,k:int):
    """Returns true if n is a prime with probability 1 - 1/4**k"""
    #T(n) = O(klog(n)**3)

    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n < 2:
        return False

    #write n on the form n = 2**r * d + 1
    r = 0
    d = n-1
    while d%2==0:
        d /= 2
        r += 1

    #probable prime satisfy a**d %n = 1 and a**(d*2**r) %n = 1
    for i in range(k):
        a = randint(2,n-2)
        test = __modulo(a,d,n)  #modulo is distributive
        if test == 1 or test == n-1:
            continue
        for i in range(r-1):
            test = (test**2)%n
            if test == n-1:
                test = True
                break    
        if test == True:
            continue
        return False

    return True


def __closePrime(n,sign):
    """Returns the closest prime less then or larger then n"""
    k = 4
    if n%2 == 0:
        nextp = n + 1*sign
    else:
        nextp = n + 2*sign

    while not millerRabin(nextp,k):
        nextp += 2*sign

    if not isPrime(nextp):         #Test prime with 100% certanty
        nextp = __closePrime(nextp,sign)

    return nextp


def nextPrime(n:int):
    """Returns the lowest prime number > n"""
    # T(n) = O(log(n)**4), avarege expected
    if n == 2:
        return 3
    if n == 3:
        return 5

    return __closePrime(n,1)


def prevPrime(n:int):
    """Returns the highest prime number < n"""
    # T(n) = O(log(n)**4), avarege expected
    if n <= 2:
        return None
    if n == 3:
        return 2
    if n == 5:
        return 3

    return __closePrime(n,-1)
    

def primeSieve(a:int,b:int):
    """Returns a list of primes in the interval [a,b] in rising order"""
    # T(n) = O(nlog(n))
    if b<a:
        raise ValueError

    n = b//2 - 1
    vec = [0]*n
    result = []

    for i in range(1,n):
        j = i
        while i+j+2*i*j <= n:
            vec[i+j+2*i*j - 1] = 1
            j += 1
    
    if a <= 2:
        result.append(2)

    for ii in range(n):
        if vec[ii] == 0 and 2*(ii+1)+1 >= a:
                result.append(2*(ii +1) + 1)

    if isPrime(b):
        result.append(b)

    return result


def newPrime(v):
    """Generates a new prime number from a given set of primes using Euclid's proof"""
    # T(n) = W(sqrt(n)), where n is resulting produkt 
    result = 1
    for i in v:
        result *= i
        if not millerRabin(i,10):
            raise ValueError("List input may only contain prime number")
    result += 1

    if result%2==0:
        return 2
    if result%3==0:
        return 3

    ii = 5
    while ii**2 <= result:
        if result % ii == 0:
            result = ii
            break
        if result % (ii+2) == 0:
            result = ii + 2
            break
        ii += 6
        
    return result


