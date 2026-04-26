class Solution:
    def numberOfWays(self, n: int) -> int:
        dp = lambda x: (x//2*2+2 - x//6*3) * (x//6+1) // 2
        res, mod = dp(n), 10**9+7
        if n >= 4:  res += dp(n-4)
        if n >= 8:  res += dp(n-8)
        return res % mod
        
class Solution2:
    def numberOfWays(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        if len(dp) > 4:
            dp[4] = 1
        if len(dp) > 8:
            dp[8] = 1

        for coin in [1, 2, 6]:
            for i in range(len(dp)):
                if i + coin < len(dp):
                    dp[i + coin] += dp[i]

        return dp[-1] % (10**9 + 7)