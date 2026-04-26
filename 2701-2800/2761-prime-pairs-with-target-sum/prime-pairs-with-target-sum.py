def getPrimes(n):
    primes = bytearray([1]) * (n + 1)
    primes[0] = primes[1] = 0
    
    for p in range(2, int(math.isqrt(n)) + 1):
        if primes[p]:
            primes[p*p:n+1:p] = bytearray(len(range(p*p, n+1, p)))
    
    return primes

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        res, primes = [], getPrimes(n)
        for i in range(2, n//2 + 1):
            if primes[i] and primes[n-i]:
                res.append([i, n-i])
        
        return res