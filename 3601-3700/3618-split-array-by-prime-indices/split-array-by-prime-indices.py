class Solution:
    def getPrimes(self, n: int) -> List[List[int]]:
        is_prime = bytearray([1]) * (n + 1)
        is_prime[0] = is_prime[1] = 0
        
        for p in range(2, math.isqrt(n) + 1):
            if is_prime[p]:
                is_prime[p*p : n+1 : p] = bytearray(len(range(p*p, n+1, p)))

        return is_prime
    
    def splitArray(self, nums: List[int]) -> int:
        sumA, sumB = 0, 0
        primes = self.getPrimes(len(nums))
        for i, n in enumerate(nums):
            if primes[i]:
                sumA += n
            else:
                sumB += n
        
        return abs(sumA - sumB)