class Solution:
    def minOperations(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        last = [0] * n
        M = 0
        for i in range(m):
            dp = [0] * n
            for j in range(n):
                if s[i] == t[j]:
                    dp[j] = 1 + (last[j-1] if j - 1 >= 0 else 0)
                    M = max(M, dp[j])
            last = dp
        return m + n - 2 * M