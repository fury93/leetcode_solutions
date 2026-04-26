class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] > k:
                    continue
                dp[i][j] = dp[i][j-1] + 1 if j - 1 >= 0 and grid[i][j-1] >= grid[i][j] else 1

        return self.numSubmat(list(zip(*dp)))

    def numSubmat(self, dp: List[List[int]]) -> int:
        m, n = len(dp), len(dp[0])
        res = 0
        for i in range(m):
            st = []
            count = 0
            for j in range(n):
                while st and dp[i][st[-1]] >= dp[i][j]:
                    r = st.pop()
                    l = st[-1] if st else -1
                    count -= (dp[i][r] - dp[i][j]) * (r - l)

                st.append(j)
                count += dp[i][j]
                res += count

        return res