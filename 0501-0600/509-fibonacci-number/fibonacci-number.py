class Solution:
    # Top-down
    def fib2(self, n: int) -> int:
        if n < 2: return n
        d = [None] * (n+1)
        d[0] = 0
        d[1] = 1
        
        def f(n):
            if n in d:
                return d[n]
            d[n] = f(n-1) + f(n-2)
            return d[n]
        
        return f(n)

    def fib(self, n: int) -> int:
        if n < 2: return n

        # order is prev1, prev2, cur
        prev1, prev2 = 0, 1
        for i in range(2, n+1):
            prev1, prev2 = prev2, prev1 + prev2

        return prev2