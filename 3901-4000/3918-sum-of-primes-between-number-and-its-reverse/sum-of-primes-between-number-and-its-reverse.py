class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        nr = int(str(n)[::-1])
        start, end = min(n, nr), max(n, nr)
        
        def getPrimes(n):
            primes = bytearray([True]) * (n + 1)
            primes[0] = primes[1] = False
            for p in range(2, math.isqrt(n) + 1):
                primes[p*p : n+1 : p] = bytearray((n - p*p) // p + 1)
            
            return [p for p, isPrime in enumerate(primes) if isPrime]

        primes = getPrimes(end)
        l = bisect_left(primes, start)
        r = bisect_right(primes, end)
        
        return sum(primes[l:r])