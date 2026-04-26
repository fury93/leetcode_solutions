class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        primes = set()
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                n = int(s[i:j])
                if Solution.isPrime(n) and n not in primes:
                    primes.add(n)

        primes = sorted(primes, reverse = True)

        return sum(primes[:3])

    @staticmethod
    @cache
    def isPrime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True