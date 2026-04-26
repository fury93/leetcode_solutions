class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res= 0
        N = len(grid[0])
        r = N-1
        for row in grid:
            l = 0
            while l <= r:
                m = l + (r-l) // 2
                if row[m] >= 0:
                    l = m + 1
                else:
                    r = m - 1
            res += N - l
            r = min(l, N-1)

        return res