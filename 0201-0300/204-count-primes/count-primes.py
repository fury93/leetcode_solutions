class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, math.isqrt(n) + 1):
            if not primes[i]: continue
            for j in range(i*i, n, i):
                primes[j] = False
        
        return sum(primes)