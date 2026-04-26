class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]

        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = suffix
                suffix = (suffix * grid[i][j]) % MOD

        prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = (p[i][j] * prefix) % MOD
                prefix = (prefix * grid[i][j]) % MOD

        return p
        
    def constructProductMatrix2(self, grid: List[List[int]]) -> List[List[int]]:
        
        it_fwd = (elem for row in grid for elem in row)
        it_rev = (elem for row in reversed(grid) for elem in reversed(row))
        
        prefix = list(accumulate(it_fwd, lambda x, y: (x * y) % 12345, initial=1))
        suffix = list(accumulate(it_rev, lambda x, y: (x * y) % 12345, initial=1))

        m,n = len(grid), len(grid[0])
        for i,j in product(range(m), range(n)):
            k = i * n + j
            grid[i][j] = (prefix[k] * suffix[-k-2]) % 12345
        
        return grid