class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        nr = int(str(n)[::-1])
        start, end = min(n, nr), max(n, nr)
        
        primes = bytearray([True]) * (end + 1)
        primes[0] = primes[1] = False
        for p in range(2, math.isqrt(end) + 1):
            primes[p*p : end+1 : p] = bytearray((end - p*p) // p + 1)

        return sum(v for v, isPrime in enumerate(primes) if isPrime and start <= v <= end)