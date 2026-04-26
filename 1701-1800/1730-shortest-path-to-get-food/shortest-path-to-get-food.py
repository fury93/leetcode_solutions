class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        # Our four permitted directions.
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        q = collections.deque()
        # Find the starting position and add to the queue.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '*':
                    q.append((row, col, 0))
                    break
        
        while q:
            r, c, steps = q.popleft()
            for y, x in dirs:
                nr = y + r
                nc = x + c
				# Ensure that the new row and col is in the grid and an unvisited or food node.
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] in ('#','O'):
				    # We found food, we're done.
                    if grid[nr][nc] == '#':
                        return steps + 1
					# Mark as visited so we don't visit again.
                    grid[nr][nc] = '|'
                    q.append((nr, nc, steps + 1))
        # We ran out of locations and found no food.
        return -1