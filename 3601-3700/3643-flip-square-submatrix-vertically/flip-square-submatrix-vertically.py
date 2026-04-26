class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        x1, x2, y2 = x, x + k - 1, y + k

        while x1 < x2:
            grid[x1][y:y2], grid[x2][y:y2] = grid[x2][y:y2], grid[x1][y:y2]
            x1, x2 = x1 + 1, x2 - 1

        return grid
