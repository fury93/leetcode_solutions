class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i, j in product(range(2),range(2)):
            block = grid[i][j] + grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1]
            if block.count('B') != 2: return True
            
        return False