class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        def backtrack(n, factors):
            if n == 1:
                if factors:
                    res.append(factors.copy())
                return

            start = factors[-1] if factors else 2
            end = n+1 if factors else n
            for factor in range(start, end):
                if n % factor == 0:
                    factors.append(factor)
                    backtrack(n // factor, factors)
                    factors.pop()
        
        backtrack(n, [])
        return res

