from itertools import product
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res, R, C = 0, len(grid), len(grid[0])
        
        for x, y in product(range(R), range(C)):
            if grid[x][y] == 0: continue
            curPer = 4
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                xx, yy = x + dx, y + dy
                if 0 <= xx < R and 0 <= yy < C and grid[xx][yy] == 1:
                    curPer -= 1
            res += curPer

        return res