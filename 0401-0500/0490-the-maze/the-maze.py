from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        ROWS, COLS = len(maze), len(maze[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visit = set()

        def dfs(r, c):
            # If we've reached the destination
            if (r, c) == (destination[0], destination[1]):
                return True
            
            # Mark this cell as visited
            visit.add((r, c))

            # Explore all four directions
            for dr, dc in directions:
                newR, newC = r, c
                
                # Roll the ball until it hits a wall
                while 0 <= newR + dr < ROWS and 0 <= newC + dc < COLS and maze[newR + dr][newC + dc] == 0:
                    newR += dr
                    newC += dc
                
                # Check if we have already visited this cell
                if (newR, newC) not in visit:
                    if dfs(newR, newC):
                        return True
            
            return False

        return dfs(start[0], start[1])
        
class Solution1:
    def dfs(self, m, n, maze, curr, destination, visit):
        if visit[curr[0]][curr[1]]:
            return False
        if curr[0] == destination[0] and curr[1] == destination[1]:
            return True

        visit[curr[0]][curr[1]] = True
        dirX = [0, 1, 0, -1]
        dirY = [-1, 0, 1, 0]

        for i in range(4):
            r = curr[0]
            c = curr[1]
            # Move the ball in the chosen direction until it can.
            while r >= 0 and r < m and c >= 0 and c < n and maze[r][c] == 0:
                r += dirX[i]
                c += dirY[i]
            # Revert the last move to get the cell to which the ball rolls.
            if self.dfs(m, n, maze, [r - dirX[i], c - dirY[i]], destination, visit):
                return True
        return False

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        visit = [[False] * n for _ in range(m)]
        return self.dfs(m, n, maze, start, destination, visit)

class Solution2:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if start == destination: return True
        
        rows, cols, processed = len(maze), len(maze[0]), -1
        q = deque([start])

        while q:
            r, c = q.popleft() # r - rows, c - cols
            #print('start', r, c, q)

            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                rr, cc = r + dr, c + dc
                while 0 <= rr < rows and 0 <= cc < cols and maze[rr][cc] != 1:
                    rr, cc = rr + dr, cc + dc
                rr, cc = rr - dr, cc - dc # how to get rid of this line ?
                #print(rr, cc)

                if rr == destination[0] and cc == destination[1]: return True
                if maze[rr][cc] == 0:
                    q.append((rr, cc))
            
            maze[r][c] = processed
                

        return False


