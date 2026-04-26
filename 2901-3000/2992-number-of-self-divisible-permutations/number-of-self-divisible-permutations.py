import math
from functools import lru_cache

class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        # Precompute allowed numbers for each position
        allowed_numbers = [[] for _ in range(n + 1)]
        for pos in range(1, n + 1):
            for num in range(1, n + 1):
                if num == 1 or math.gcd(num, pos) == 1:
                    allowed_numbers[pos].append(num)
        
        @lru_cache(maxsize=None)
        def dp(pos: int, mask: int) -> int:
            if pos > n:
                return 1  # All positions are filled successfully
            total = 0
            for num in allowed_numbers[pos]:
                bit = 1 << (num - 1)
                if not (mask & bit):
                    total += dp(pos + 1, mask | bit)
            return total
        
        return dp(1, 0)
        
class Solution2:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        from math import gcd
        all_nums = set(range(1, n + 1))
        self.output = 0

        def backtrack(path, N):
            if len(path) == n:
                self.output += 1
            else:
                for num in all_nums:
                    if num not in path and gcd(num, N) == 1:
                        backtrack(path + [num], N + 1)

        backtrack([], 1)
        return self.output

