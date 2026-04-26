class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[[None]*4 for _ in range(n)] for _ in range(n)]
        mines = {(i, j) for i, j in mines}
        # right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def getArm(i, j, d):
            if not (0 <= i < n and 0 <= j < n) or (i,j) in mines:
                return 0
            if dp[i][j][d] is None:
                di, dj = i + directions[d][0], j + directions[d][1]
                dp[i][j][d] = 1 + getArm(di, dj, d)
            
            return dp[i][j][d]
        
        maxRank = 0
        for i, j in product(range(n), range(n)):
            rank = min(getArm(i, j, d) for d in range(4))
            maxRank = max(maxRank , rank)
        
        return maxRank