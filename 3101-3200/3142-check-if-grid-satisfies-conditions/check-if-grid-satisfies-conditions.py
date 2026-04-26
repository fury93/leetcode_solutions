class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for a, b in pairwise(grid[0]):
            if a == b: return False
        
        for coll in zip(*grid):
            if not all(coll[0] == cell for cell in coll): return False

        return True
