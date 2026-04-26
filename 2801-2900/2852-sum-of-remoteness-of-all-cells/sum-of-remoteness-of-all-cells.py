class UnionFind:

    def __init__(self, n: int):
        self.root = list(range(n))
        self.rank = [1 for _ in range(n)]

    def find(self, x: int) -> int:
        if x != self.root[x]: self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty: return
        if rootx > rooty: self.root[rooty] = rootx
        elif rootx < rooty: self.root[x] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
    
    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n * n)
        directions = [(-1, 0), (0, 1)]
        s = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == -1: continue
                s += grid[i][j]
                for di, dj in directions:
                    ci, cj = i + di, j + dj
                    if 0 <= ci < n and 0 <= cj < n and grid[ci][cj] != -1:
                        uf.union(i * n + j, ci * n + cj)
        s_g = [0 for _ in range(n * n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == -1: continue
                s_g[uf.find(i * n + j)] += grid[i][j]
        
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == -1: continue
                res += s - s_g[uf.find(i * n + j)]
        return res