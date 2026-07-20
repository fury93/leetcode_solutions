class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        res = [[0] * C for _ in range(R)]
        L = R*C
        k = k % L

        for i in range(L):
            new_id = (i+k) % L
            res[new_id//C][new_id%C] = grid[i//C][i%C]
        
        return res