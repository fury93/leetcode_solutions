class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def getFish(x, y):
            fish, grid[x][y] = grid[x][y], 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                xx, yy = x + dx, y + dy
                if 0 <= xx < R and 0 <= yy < C and grid[xx][yy] > 0:
                    fish += getFish(xx, yy)
            
            return fish
        
        res = 0
        for x, y in itertools.product(range(R), range(C)):
            if grid[x][y] > 0:
                res = max(res, getFish(x, y))

        return res