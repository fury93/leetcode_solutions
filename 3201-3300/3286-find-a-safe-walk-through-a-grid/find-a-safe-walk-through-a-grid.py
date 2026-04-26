# 0-1 BFS
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        MAX_DAMAGE = rows + cols + 1
        q = deque([(0, 0)])
        damage = [[MAX_DAMAGE] * cols for _ in range(rows)]
        damage[0][0] = grid[0][0]

        while q:
            r, c = q.popleft()
            
            if r == rows - 1 and c == cols - 1:
                return damage[-1][-1] < health

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    newDamage = grid[nr][nc]
                    if damage[r][c] + newDamage < damage[nr][nc]:
                        damage[nr][nc] = damage[r][c] + newDamage
                        
                        if newDamage:
                            q.append((nr, nc))
                        else:
                            q.appendleft((nr, nc))

        return False
        
# Dijkstra
class Solution2:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        INF = rows + cols + 1
        rows, cols = len(grid), len(grid[0])
        pq = [(grid[0][0], 0, 0)]
        # how many health we lost to get to this cell
        visited = [[INF] * cols for _ in range(rows)]

        while pq:
            h, r, c = heappop(pq)
            if visited[r][c] < h: continue

            if r == rows - 1 and c == cols - 1:
                return h < health

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    nh = h + grid[nr][nc]
                    if nh < health and nh < visited[nr][nc]:
                        visited[nr][nc] = nh
                        heappush(pq, (nh, nr, nc))

        return False