class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0: return False
        N = len(grid)
        moves = [None] * N**2

        for r, c in product(range(N), range(N)):
            moves[grid[r][c]] = (r, c)

        for prev, cur in pairwise(moves):
            if abs(prev[0] - cur[0]) *  abs(prev[1] - cur[1]) != 2:
                return False

        return True
