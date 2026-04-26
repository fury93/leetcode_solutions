class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque((r, c) for r, c in product(range(N), range(N)) if grid[r][c] == 1)
        if len(q) == N * N or len(q) == 0:
            return -1
        
        res = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
                    q.append((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1
                    res = grid[nr][nc]
        
        return res - 1