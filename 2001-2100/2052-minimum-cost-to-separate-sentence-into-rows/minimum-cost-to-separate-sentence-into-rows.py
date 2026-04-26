class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:
        if len(sentence) <= k:
            return 0
        words = sentence.split()
        n = len(words)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(1, n):
            length = 0
            for j in range(i - 1, -1, -1):
                length += len(words[j])
                if j < i - 1:
                    length += 1
                if length > k:
                    break
                dp[i] = min(dp[i], (k - length) ** 2 + dp[j])
        ans, length = dp[-1], len(words[-1])
        for j in range(n - 2, -1, -1):
            length += 1 + len(words[j])
            if length > k:
                break
            ans = min(ans, dp[j])
        return ans