class Solution:
    def numberOfWays(
        self, n: int, m: int, k: int, source: List[int], dest: List[int]
    ) -> int:
        a, b, c, d = 1, 1, 0, 0
        M = 10**9 + 7
        for i in range(2, k + 1):
            d_ = ((m + n - 4) * d + a + b) % M
            c_ = ((m - 1) * b + (n - 1) * a) % M
            a_ = ((m - 1) * d + (n - 2) * a + c) % M
            b_ = ((n - 1) * d + (m - 2) * b + c) % M
            a, b, c, d = a_, b_, c_, d_
        if source == dest:
            return c
        if dest[0] == source[0]:
            return b
        if dest[1] == source[1]:
            return a
        return d
        
class Solution2:
    def numberOfWays(self, n: int, m: int, k: int, source: List[int], dest: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0]*4 for _ in range(k+1)]
        if source == dest:
            dp[0][0] = 1
        elif source[0] == dest[0]:
            dp[0][1] = 1
        elif source[1] == dest[1]:
            dp[0][2] = 1
        else:
            dp[0][3] = 1
        for i in range(1, k+1):
            dp[i][0] = (dp[i-1][1] + dp[i-1][2])%MOD
            dp[i][1] = (dp[i-1][0]*(m-1) + dp[i-1][1]*(m-2) + dp[i-1][3])%MOD
            dp[i][2] = (dp[i-1][0]*(n-1) + dp[i-1][2]*(n-2) + dp[i-1][3])%MOD
            dp[i][3] = (dp[i-1][1]*(n-1) + dp[i-1][2]*(m-1) + dp[i-1][3]*(m+n-4))%MOD
        return dp[k][0]

            