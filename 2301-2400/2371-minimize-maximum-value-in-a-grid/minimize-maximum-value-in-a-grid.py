class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        vals = [(grid[i][j],i,j) for i in range(m) for j in range(n)]
        row_max,col_max = [0]*m,[0]*n
        for _,i,j in sorted(vals):
            v = max(row_max[i],col_max[j])+1
            row_max[i],col_max[j]=v,v
            grid[i][j]=v
        return grid

class Solution1:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = len(grid), len(grid[0])

        nums = []
        # Create rows and cols to store the minimum values for every row and column.
        rows = [1 for i in range(row)]
        cols = [1 for i in range(col)]

        # Create a matrix nums that stores the values of the matrix and their indices.
        for i in range(row):
            for j in range(col):
                nums.append((grid[i][j], i, j))

        nums.sort()
        for tup in nums:
            _, i, j = tup
            # Find the maximum value of rows[i] and cols[j] till now and assign it to val.
            val = max(rows[i], cols[j])
            grid[i][j] = val
            # Update the new maximum value in rows[i] and cols[j].
            rows[i], cols[j] = val + 1, val + 1
        return grid

class Solution2:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        row_size, col_size = len(grid), len(grid[0])

        # Min-heap to store elements with their values and coordinates
        min_heap = []
        # Initialize rows and cols arrays to keep track of maximum values assigned
        rows = [1] * row_size
        cols = [1] * col_size

        # Populate the min-heap with all elements of the grid
        for i in range(row_size):
            for j in range(col_size):
                heapq.heappush(min_heap, (grid[i][j], i, j))

        # Process elements in ascending order of their values
        while min_heap:
            _, i, j = heapq.heappop(min_heap)
            # Determine the smallest assignable value based on rows and cols constraints
            val = max(rows[i], cols[j])
            grid[i][j] = val
            # Update rows and cols arrays with the next possible value for each row and column
            rows[i] = val + 1
            cols[j] = val + 1

        return grid