class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        # 1. write a boolean fn to produce order/monotonicity
        def fulfill(s):
            res = 0
            for row in grid:
                res += bisect.bisect_right(row, s)
            return res >= m * n // 2 + 1
        
        # 2. locate search space and do search range shrinkage, do proper return
        low, high = 0, 10 ** 6 + 1
        while low < high:
            mid = low + (high - low) // 2
            if fulfill(mid):
                high = mid
            else:
                low = mid + 1
        return high