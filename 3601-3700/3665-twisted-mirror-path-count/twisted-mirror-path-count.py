class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        curRow = [0] * n
        curRow[0] = 1
        for row in grid:
            prvRow, curRow, prvCel = curRow, [0] * n, 0
            
            for idx, p in enumerate(prvRow):
                if row[idx] == 0:
                    curRow[idx], prvCel = prvCel + p, prvCel + p
                else:
                    curRow[idx], prvCel = prvCel, p

        return curRow[-1] %1_000_000_007
        
    def uniquePaths2(self, grid: List[List[int]]) -> int:
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