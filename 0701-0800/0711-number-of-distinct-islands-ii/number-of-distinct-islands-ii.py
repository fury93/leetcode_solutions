class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        def dfs(x, y, coords):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return
            grid[x][y] = 0
            coords.append((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy, coords)

        def canonical(coords):
            shapes = []
            for i, j in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                # Reflection
                shape = sorted([(x * i, y * j) for x, y in coords])
                shape = [(x - shape[0][0], y - shape[0][1]) for x, y in shape]
                shapes.append(shape)

                # Rotations
                shape = sorted([(y * i, x * j) for x, y in coords])
                shape = [(x - shape[0][0], y - shape[0][1]) for x, y in shape]
                shapes.append(shape)
                
            return min(shapes)

        distinct_islands = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    coords = []
                    dfs(x, y, coords)
                    distinct_islands.add(tuple(canonical(coords)))

        return len(distinct_islands)