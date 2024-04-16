import primeLib as p

#Unit test
def testisPrime():  

    #test for some regular prime
    assert p.isPrime(2)
    assert p.isPrime(7)
    assert p.isPrime(17)
    assert p.isPrime(2**17-1) #mersenne prime
    assert p.isPrime(100040333)


    #test composits and negatives
    assert not p.isPrime(4)
    assert not p.isPrime(100555)
    assert not p.isPrime(100040331)

def testMiller():

    #test for some regular prime
    assert p.millerRabin(2,20)
    assert p.millerRabin(7,20)
    assert p.millerRabin(17,20)
    assert p.millerRabin(2**17-1,20) #mersenne prime
    assert p.millerRabin(100040333,20)

    #test composits and negatives
    assert not p.millerRabin(4,20)
    assert not p.millerRabin(100555,20)
    assert not p.millerRabin(100040331,20)


def testNextPrev():
    #Test for different size of primes
    Pe0 = [2,3,5,7,11,13,17,19]
    Pe6 = [1036613,1036619,1036631,1036649,1036661,1036667,1036669,1036681]
    Pe8 = [100001821,100001827,100001843,100001887,100001893,100001903,100001927,100001929]
    x = len(Pe0)
    for i in range(x-2):
        assert p.nextPrime(Pe0[i])==Pe0[i+1]
        assert p.nextPrime(Pe6[i])==Pe6[i+1]
        assert p.nextPrime(Pe8[i])==Pe8[i+1]

        assert p.prevPrime(Pe0[x-1-i])==Pe0[x-i-2]
        assert p.prevPrime(Pe6[x-1-i])==Pe6[x-i-2]
        assert p.prevPrime(Pe8[x-1-i])==Pe8[x-i-2]

    #test lower bound
    assert p.prevPrime(2) is None
    assert p.prevPrime(-5) is None

def testPrimeSieve():
    #test regular intervals
    assert p.primeSieve(2,19) == [2,3,5,7,11,13,17,19]
    assert p.primeSieve(-2,19) == [2,3,5,7,11,13,17,19]
    assert p.primeSieve(1036613,1036681) == [1036613,1036619,1036631,1036649,1036661,1036667,1036669,1036681]

    #test short intervals
    assert p.primeSieve(6,10) == [7]
    assert p.primeSieve(8,10) == []
    
    #test impossible intervals
    try:
        p.primeSieve(17,2)
        print("primeSiev() gives output from impossible interval (not expected)")
    except:
        pass


def testAcc():
    #Compare estimated accuracy of Miller Rabin test
    k = [1,2,4,6]
    l=[]
    l2=[]
    count = 0
    for j in k:
        for i in range(300000,500000):
            if p.millerRabin(i,j) != p.isPrime(i):
                count += 1
        l.append(count/300000)
        l2.append(1/4**j)
        print("Calculated accuracy: {} Expected accuary: {} ".format(1-count/(300000-14966),1-1/4**j))
        count = 0
    return l,l2  


def testNewPrime():
    #Test new prime for regular lists
    x = p.newPrime([2,3,5,7,19])
    assert p.isPrime(x)
    x = p.newPrime([2,3,1036613,1036619,1036631,1036649,1036661,1036667,1036669,1036681])
    assert p.isPrime(x)

    #test when the produkt +1 is a new prime
    x = p.newPrime([2,3,5])
    assert p.isPrime(x)

    #test for sparse lists
    x = p.newPrime([3])
    assert p.isPrime(x)
    assert p.newPrime([]) == 2

    #test for list containing negatives and composits
    try:
        p.newPrime([2,3,5,6,7,19])
        print("newPrime() input can contain composits (not expected)")
    except ValueError:
        pass

    try:
        p.newPrime([2,3,5,-7,19])
        print("newPrime() input can contain negative numbers (not expected)")
    except ValueError:
        pass
        

    


def main():
    testisPrime()
    testMiller()
    testNextPrev()
    testPrimeSieve()
    testAcc()
    testNewPrime()

main()


