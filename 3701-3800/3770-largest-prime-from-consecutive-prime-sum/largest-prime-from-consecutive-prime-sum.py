def getPrimes(n: int) -> List[List[int]]:
    primes = bytearray([1]) * (n + 1)
    primes[0] = primes[1] = 0
    
    for p in range(2, math.isqrt(n) + 1):
        if primes[p]:
            primes[p*p : n+1 : p] = bytearray(len(range(p*p, n+1, p)))
    return primes

class Solution:
    def largestPrime(self, n: int) -> int:
        maxPrimeSum, curSum = 0, 0
        primes = getPrimes(n)
        for i in range(2, n + 1):
            if primes[i]:
                curSum += i
                if curSum > n: break
                if primes[curSum]:
                    maxPrimeSum = curSum

        return maxPrimeSum 