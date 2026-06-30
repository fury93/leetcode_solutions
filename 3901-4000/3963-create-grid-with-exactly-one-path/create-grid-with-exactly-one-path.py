class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for i in range(m):
            row = ('#' * (n-1) + '.') if i > 0 else '.' * n
            grid.append(row)
        return grid