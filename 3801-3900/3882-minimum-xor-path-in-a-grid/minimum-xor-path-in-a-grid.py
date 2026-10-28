class Solution:
    def minCost(self, g: list[list[int]]) -> int:
        return min((f:=cache(lambda i,j:len(g)>i>=0<=j<len(g[0]) and ( 
            {g[i][j]^v for v in f(i+1,j)|f(i,j+1)} or {g[i][j]}) or set()))(0,0))

        @cache
        def f(i,j,m=len(g),n=len(g[0])):
            if i//len(g)|j//len(g[0]): return set()
            return {g[i][j]^v for v in f(i+1,j)|f(i,j+1)} or {g[i][j]}
        
        return min(f(0,0))

    def minCost2(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                value = grid[i][j]
                reachable = dp[j] | (dp[j - 1] if j > 0 else set())

                dp[j] = {k ^ value for k in reachable}

        return min(dp[-1])