class Solution:
    def numIslands2(self, rows: int, cols: int, positions: List[List[int]]) -> List[int]:
        res, uf = [], UnionFind(rows * cols)

        def getIndex(row, col):
            return row * cols + col
        
        for row, col in positions:
            idx = getIndex(row, col)
            uf.add(idx)
            for rowDiff, colDiff in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                adjacentRow, adjacentCol = row + rowDiff, col + colDiff
                if 0 <= adjacentRow < rows and 0 <= adjacentCol < cols:
                    uf.union(idx, getIndex(adjacentRow, adjacentCol))
            res.append(uf.getCount())
                    
        return res

class UnionFind:
    def __init__(self, size):
        self.root = [None for i in range(size)]
        self.rank = [0] * size
        self.cnt = 0

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        if self.root[x] is None or self.root[y] is None: return

        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.cnt -= 1

    def add(self, x):
        if self.root[x] is not None: return
        self.root[x] = x
        self.cnt += 1

    def getCount(self):
        return self.cnt