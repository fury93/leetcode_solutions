class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = [(0, 0, 1)]
        grid[0][0] = 1
        for i, j, d in q:
            if i == n-1 and j == n-1: return d
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    q.append((x, y, d+1))
        return -1
    
    def shortestPathBinaryMatrix2(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(r, c, path):
            if r < 0 or c < 0 or grid[r][c] == 1:
                return -1
            if r == 0 and c == 0:
                return path
            left = dfs(r - 1, c, path + 1)
            top = dfs(r, c - 1, path + 1)
            diag = dfs(r - 1, c - 1, path + 1)

            return min(filter(lambda x: x > 0,  [left, top, diag]), default = -1)
        
        return dfs(R - 1, C - 1, 1)


class Solution:
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:  
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        current_distance = 1
        
        # Do the BFS.
        while queue:
            # Process all nodes at current_distance from the top-left cell.
            nodes_of_current_distance = len(queue)
            for _ in range(nodes_of_current_distance):
                row, col = queue.popleft()
                if (row, col) == (max_row, max_col):
                    return current_distance
                for neighbour in get_neighbours(row, col):
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    queue.append(neighbour)
            # We'll now be processing all nodes at current_distance + 1
            current_distance += 1
                    
        # There was no path.
        return -1 