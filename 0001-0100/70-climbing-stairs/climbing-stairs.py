class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        prev1 = 1
        prev2 = 2

        for i in range(2, n):
            prev1, prev2 = prev2, prev1 + prev2
        
        return prev2

    def climbStairs2(self, n: int) -> int:
        d = {}

        def climb(n):
            if n <= 2:
                return n
            if n not in d:
                d[n] = climb(n-1) + climb(n-2)
            return d[n]

        return climb(n)