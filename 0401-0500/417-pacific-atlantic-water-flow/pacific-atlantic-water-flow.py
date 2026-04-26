class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        p_land = set()
        a_land = set()
        R, C = len(matrix), len(matrix[0])
        def spread(i, j, land):
            land.add((i, j))
            for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if (0<=x<R and 0<=y<C and matrix[x][y] >= matrix[i][j]
                        and (x, y) not in land):
                    spread(x, y, land)
                    
        for i in range(R):
            spread(i, 0, p_land)
            spread(i, C-1, a_land)
        for j in range(C):
            spread(0, j, p_land)
            spread(R-1, j, a_land)
        return list(p_land & a_land)

    def pacificAtlantic2(self, M):
        if not M or not M[0]: return []
        
        m, n = len(M[0]), len(M)
        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]:
                    if 0 <= dx < n and 0 <= dy < m and (dx, dy) not in visited and M[dx][dy] >= M[x][y]:
                        queue.append((dx, dy))
                        visited.add((dx, dy))
                        
            return list(visited)
        
        pacific  = [(0, i) for i in range(m)]   + [(i, 0) for i in range(1,n)]
        atlantic = [(n-1, i) for i in range(m)] + [(i, m-1) for i in range(n-1)]
        
        return bfs(pacific) & bfs(atlantic)