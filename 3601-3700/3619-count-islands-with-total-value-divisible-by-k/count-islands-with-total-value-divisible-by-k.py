class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        res, R, C = 0, len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c):
            total = grid[r][c]
            grid[r][c] = 0
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] > 0:
                    total += dfs(nr, nc)
            return total


        for r, c in product(range(R), range(C)):
            if grid[r][c] != 0:
                totalValue = dfs(r, c)
                res += totalValue % k == 0

        return res