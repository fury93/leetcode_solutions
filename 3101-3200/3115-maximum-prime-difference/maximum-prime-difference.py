# https://leetcode.com/u/yourick/

def getPrimes(limit):
            primes = [True] * (limit + 1)
            primes[0] = primes[1] = False
            
            for p in range(2, math.isqrt(limit) + 1):
                if primes[p]:
                    for i in range(p * p, limit + 1, p):
                        primes[i] = False
            return primes
    
PRIMES = getPrimes(100)

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        for l in range(len(nums)):
            if PRIMES[nums[l]]: break

        for r in range(len(nums)-1, -1, -1):
            if PRIMES[nums[r]]: break

        return r - l
        