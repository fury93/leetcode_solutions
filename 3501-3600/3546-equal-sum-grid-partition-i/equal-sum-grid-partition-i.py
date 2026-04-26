class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        
        total_sum = sum(sum(row) for row in grid)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2

        current_row_prefix = 0
        for i in range(rows - 1):
            current_row_prefix += sum(grid[i])
            if current_row_prefix == target:
                return True

        current_col_prefix = 0
        for j in range(cols - 1):
            current_col_sum = sum(grid[i][j] for i in range(rows))
            current_col_prefix += current_col_sum
            if current_col_prefix == target:
                return True

        return False
        