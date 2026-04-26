class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        m = len(queries)
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        nums += [-1]
        ans = 0
        
        for d in range(n - 1, -1, -1):
            for i in range(n):
                j = i + d
                if j < n:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j + 1])
                    if nums[i - 1] >= queries[dp[i - 1][j]]:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1)
                    if nums[j + 1] >= queries[dp[i][j + 1]]:
                        dp[i][j] = max(dp[i][j], dp[i][j + 1] + 1)
                    if dp[i][j] == m:
                        return m
                else:
                    break
        for i in range(n):
            ans = max(ans, dp[i][i] + (nums[i] >= queries[dp[i][i]]))
        return ans