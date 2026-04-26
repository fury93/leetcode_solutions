class Solution:
    def peopleAwareOfSecret(self, n: int, dd: int, ff: int) -> int:
        dp, mod = [0] * 1002, 1000000007
        dp[1], dp[2] = 1, -1
        cur, ans = 0, 0
        
        for d in range(1, n + 1):
            cur += dp[d]
            if d + ff > n:
                ans += cur
            if cur > 0:
                dp[min(d + dd, 1001)] += cur
                dp[min(d + ff, 1001)] -= cur

        return ans % mod