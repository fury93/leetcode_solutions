class Solution:
    def swimInWater(self, grid):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pq = [(grid[0][0], 0, 0)] # (time, row, col)
        N = len(grid)
        visited = set([(0, 0)])
        maxTime = grid[0][0]

        def isValid(row, col):
            return (row, col) not in visited and 0 <= row < N and 0 <= col < N

        while True:
            curTime, r, c = heapq.heappop(pq)
            maxTime = max(maxTime, curTime)

            if r == N - 1 and c == N - 1: break

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not isValid(nr, nc): continue

                heapq.heappush(pq, (grid[nr][nc], nr, nc))
                visited.add((nr, nc))

        return maxTime