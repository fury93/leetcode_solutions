class Solution:
    # Kahn algo
    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        indegree = [[0] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(m):
            for j in range(n):
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[i][j]:
                        indegree[i][j] += 1
 
        # Start the topological sort with cells of zero indegree
        queue = deque([[x, y] for x in range(m) for y in range(n) if indegree[x][y] == 0])

        max_inc_path = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                        indegree[ni][nj] -= 1
                        if indegree[ni][nj] == 0:
                            queue.append((ni, nj))
            max_inc_path += 1
        return max_inc_path

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = [[None] * cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if cache[r][c]: 
                return cache[r][c]

            maxPath = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[r][c] < matrix[nr][nc]:
                    maxPath = max(maxPath, 1 + dfs(nr, nc))

            cache[r][c] = maxPath
            return cache[r][c]

        for r, c in product(range(rows), range(cols)):
            if not cache[r][c]:
                dfs(r, c)

        return max(map(max, cache))