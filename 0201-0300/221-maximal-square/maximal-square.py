class Solution:
    def maximalSquare(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        maxSide, prev = 0, 0
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                savedPrev = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = min(prev, dp[j - 1], dp[j]) + 1
                    maxSide = max(maxSide, dp[j])
                else:
                    dp[j] = 0
                prev = savedPrev
        return maxSide**2

class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 # Be careful of the indexing since dp grid has additional row and column
                    max_side = max(max_side, dp[r+1][c+1])
                
        return max_side * max_side
                