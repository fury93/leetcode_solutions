class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def isPrime(n):
            if n <= 1: return False
            if n <= 3: return True
            if n % 2 == 0 or n % 3 == 0: return False

            # all primes is 6k ± 1, i = 6k - 1
            for i in range(5, math.isqrt(n)+1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False

            return True

        return any(isPrime(v) for v in Counter(nums).values())