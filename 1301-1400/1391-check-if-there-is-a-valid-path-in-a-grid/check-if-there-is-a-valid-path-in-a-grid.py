class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        w, n, e, s = 0, 1, 2, 3

        # (dy, dx, next entrance)
        to_east = (0, 1, w)
        to_west = (0, -1, e)
        to_north = (-1, 0, s)
        to_south = (1, 0, n)

        # (0 - from west, 1 - from north, 2 - from east, 3 - from south)
        path = [None,
            (to_east, None, to_west, None),   # 1═
            (None, to_south, None, to_north), # 2║
            (to_south, None, None, to_west),  # 3╗
            (None, None, to_south, to_east),  # 4╔
            (to_north, to_west, None, None),  # 5╝
            (None, to_east, to_north, None),  # 6╚
        ]

        M, N = len(grid), len(grid[0])

        for side in w, n, e, s:
            r, c = 0, 0

            while 0 <= r < M and 0 <= c < N:
                if path[grid[r][c]][side] is None: break
                if r == M - 1 and c == N - 1: return True

                dy, dx, side = path[grid[r][c]][side]
                r, c = r + dy, c + dx

                if r == 0 and c == 0: return False

        return False
        
class Solution2:
    class DisjointSet:
        def __init__(self, n):
            self.f = list(range(n))

        def find(self, x):
            if x == self.f[x]:
                return x
            self.f[x] = self.find(self.f[x])
            return self.f[x]

        def merge(self, x, y):
            self.f[self.find(x)] = self.find(y)

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        patterns = [0, 0b1010, 0b0101, 0b1100, 0b0110, 0b1001, 0b0011]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ds = Solution.DisjointSet(m * n)

        def getId(x, y):
            return x * n + y

        def handler(x, y):
            pattern = patterns[grid[x][y]]
            for i, (dx, dy) in enumerate(dirs):
                if (pattern & (1 << i)) > 0:
                    sx, sy = x + dx, y + dy
                    if (
                        0 <= sx < m
                        and 0 <= sy < n
                        and (patterns[grid[sx][sy]] & (1 << ((i + 2) % 4))) > 0
                    ):
                        ds.merge(getId(x, y), getId(sx, sy))

        for i in range(m):
            for j in range(n):
                handler(i, j)

        return ds.find(getId(0, 0)) == ds.find(getId(m - 1, n - 1))