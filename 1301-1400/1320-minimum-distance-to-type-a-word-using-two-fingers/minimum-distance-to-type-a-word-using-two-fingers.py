class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        BIG = 2**30
        dp = [[0] * 26] + [[BIG] * 26 for _ in range(n - 1)]

        def getDistance(p, q):
            x1, y1 = p // 6, p % 6
            x2, y2 = q // 6, q % 6
            return abs(x1 - x2) + abs(y1 - y2)

        for i in range(1, n):
            cur, prev = ord(word[i]) - 65, ord(word[i - 1]) - 65
            d = getDistance(prev, cur)
            for j in range(26):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + d)
                if prev == j:
                    for k in range(26):
                        d0 = getDistance(k, cur)
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + d0)

        ans = min(dp[n - 1])
        return ans