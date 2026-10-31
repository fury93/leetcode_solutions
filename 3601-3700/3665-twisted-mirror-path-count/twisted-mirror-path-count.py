class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        f = [[0, 0] for _ in range(n)]
        f[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    if grid[i - 1][j] == 0:
                        f[j][0] = (f[j][0] + f[j][1]) % MOD
                    else:
                        f[j][0] = f[j][1]

                if j > 0:
                    if grid[i][j - 1] == 0:
                        f[j][1] = (f[j - 1][0] + f[j - 1][1]) % MOD
                    else:
                        f[j][1] = f[j - 1][0]

        return (f[-1][0] + f[-1][1]) % MOD