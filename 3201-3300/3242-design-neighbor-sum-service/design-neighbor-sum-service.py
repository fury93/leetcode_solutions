class NeighborSum2:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.size = len(grid)
        self.positions = [None] * self.size ** 2
        self.adjacent = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.diagonal = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
        
        for i, j in product(range(self.size), range(self.size)):
            self.positions[grid[i][j]] = i, j

    def adjacentSum(self, value: int) -> int:
        return self.calculateSum(value, self.adjacent)

    def diagonalSum(self, value: int) -> int:
        return self.calculateSum(value, self.diagonal)
        
    def calculateSum(self, value, neighborDiff):
        i, j = self.positions[value]
        sm = 0
        for di, dj in neighborDiff:
            ii, jj = i + di, j + dj
            if 0 <= ii < self.size and 0 <= jj < self.size:
                sm += self.grid[ii][jj]
        return sm

class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.size = len(grid)
        self.positions = [None] * self.size ** 2
        
        for i, j in product(range(self.size), range(self.size)):
            self.positions[grid[i][j]] = i, j

    def adjacentSum(self, value: int) -> int:
        i, j = self.positions[value]
        sm = 0
        sm += self.grid[i-1][j] if i >= 1 else 0 # top
        sm += self.grid[i+1][j] if i+1 < self.size else 0 # bottom
        sm += self.grid[i][j-1] if j >= 1 else 0 # left
        sm += self.grid[i][j+1] if j+1 < self.size else 0 # right

        return sm

        

    def diagonalSum(self, value: int) -> int:
        i, j = self.positions[value]
        sm = 0
        sm += self.grid[i-1][j-1] if i >= 1 and j >= 1 else 0 # top left
        sm += self.grid[i+1][j+1] if i+1 < self.size and j+1 < self.size else 0 # bottom right
        sm += self.grid[i-1][j+1] if i >= 1 and j+1 < self.size else 0 # top right
        sm += self.grid[i+1][j-1] if i+1 < self.size and j >= 1 else 0 # bottome left

        return sm
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)