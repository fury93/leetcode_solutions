class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n) % 2 == 0:
            return False

        target = (m + n - 1) / 2
        
        @cache
        def helper(y, x, summ):
            if not (0 <= y < m and 0 <= x < n):
                return False
            
            summ += grid[y][x]
            if y == m - 1 and x == n - 1 and summ == target:
                return True

            return helper(y + 1, x, summ) or helper(y, x + 1, summ)
        
        return helper(0, 0, 0)

class Solution2:
    def isThereAPath(self, grid: list[list[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        if (rows + cols) % 2 == 0:
            return False

        min_ = [[0] * cols for _ in range(rows)]
        max_ = [[0] * cols for _ in range(rows)]

        min_[0][0] = max_[0][0] = grid[0][0]

        for row in range(1, rows):
            min_[row][0] = min_[row - 1][0] + grid[row][0]
            max_[row][0] = max_[row - 1][0] + grid[row][0]

        for col in range(1, cols):
            min_[0][col] = min_[0][col - 1] + grid[0][col]
            max_[0][col] = max_[0][col - 1] + grid[0][col]

        for row in range(1, rows):
            for col in range(1, cols):
                min_prev = min(min_[row - 1][col], min_[row][col - 1])
                min_[row][col] = min_prev + grid[row][col]

                max_prev = max(max_[row - 1][col], max_[row][col - 1])
                max_[row][col] = max_prev + grid[row][col]

        target = (rows + cols - 1) // 2
        return min_[rows - 1][cols - 1] <= target <= max_[rows - 1][cols - 1]