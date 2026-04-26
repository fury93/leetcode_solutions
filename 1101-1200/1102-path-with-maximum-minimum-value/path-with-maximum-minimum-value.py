# TLE
class Solution1:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        # 4 directions to a cell's possible neighbors.
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Check if we can find a path of score equals val.
        def path_exists(cur_score):

            # Maintain the visited status of each cell. Initalize the status of
            # all the cells as false (unvisited).
            visited = [[False] * C for _ in range(R)]
            visited[0][0] = True

            # Put the starting cell grid[0][0] in the deque and mark it as visited.
            dq = collections.deque([(0, 0)])

            # While we still have cells of value larger than or equal to val.
            while dq:
                cur_row, cur_col = dq.popleft()

                # If the current cell is the bottom-right cell, return true.
                if cur_row == R - 1 and cur_col == C - 1:
                    return True
                for d_row, d_col in dirs:
                    new_row = cur_row + d_row
                    new_col = cur_col + d_col

                    # Make sure (new_row, new_col) is on the grid.
                    if not (0 <= new_row < R and 0 <= new_col < C):
                        continue

                    # Check if the current cell has any unvisited neighbors
                    # with value greater than or equal to cur_score.
                    if (
                        grid[new_row][new_col] >= cur_score
                        and not visited[new_row][new_col]
                    ):
                        # If so, we put this neighbor to the deque and mark it as visited
                        visited[new_row][new_col] = True
                        dq.append((new_row, new_col))
            return False

        cur_score = min(grid[0][0], grid[R - 1][C - 1])

        # Start with "cur_score", check if we can find a path of score equals cur_score.
        # If so, return cur_score as the maximum score, otherwise, decrease cur_score
        # by 1 and repeat these steps.
        while cur_score >= 0:
            if path_exists(cur_score):
                return cur_score
            else:
                cur_score -= 1

class Solution2:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        # 4 directions to a cell's possible neighbors.
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Check if we can find a path of value = cur_score.
        def path_exists(cur_score):
            dq = collections.deque()
            visited = [[False] * C for _ in range(R)]

            # Put the starting cell grid[0][0] in the deque and mark it as visited.
            visited[0][0] = True
            dq.append((0, 0))

            # While we still have cells of value larger than or equal to val.
            while dq:
                cur_row, cur_col = dq.popleft()

                # If the current cell is the bottom-right cell, return true.
                if cur_row == R - 1 and cur_col == C - 1:
                    return True
                for d_row, d_col in dirs:
                    new_row = cur_row + d_row
                    new_col = cur_col + d_col

                    # Make sure (new_row, new_col) is on the grid.
                    if not (0 <= new_row < R and 0 <= new_col < C):
                        continue

                    # Check if the current cell has any unvisited neighbors
                    # with value greater than or equal to cur_score.
                    if (
                        grid[new_row][new_col] >= cur_score
                        and not visited[new_row][new_col]
                    ):
                        # If so, we put this neighbor to the deque and mark it as visited.
                        visited[new_row][new_col] = True
                        dq.append((new_row, new_col))
            return False

        left = 0
        right = min(grid[0][0], grid[-1][-1])

        while left < right:
            # Get the middle value between left and right boundaries.
            middle = (left + right + 1) // 2

            # Check if we can find a path with value = middle, and cut
            # the search space by half.
            if path_exists(middle):
                left = middle
            else:
                right = middle - 1

        # Once the left and right boundaries coincide, we find the target value,
        # that is, the maximum value of a path.
        return left

class Solution3:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        # 4 directions to a cell's possible neighbors.
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Check if we can find a path of value = val.
        def path_exists(val):
            visited = [[False] * C for _ in range(R)]

            def dfs(cur_row, cur_col):
                # If we reach the bottom-right cell, return true.
                if cur_row == R - 1 and cur_col == C - 1:
                    return True

                # Mark the current cell as visited.
                visited[cur_row][cur_col] = True
                for d_row, d_col in dirs:
                    new_row = cur_row + d_row
                    new_col = cur_col + d_col

                    # Make sure (new_row, new_col) is on the grid and has not been visited.
                    if (
                        not (0 <= new_row < R and 0 <= new_col < C)
                        or visited[new_row][new_col]
                    ):
                        continue

                    # Check if the current cell has any unvisited neighbors
                    # with value greater than or equal to val.
                    if grid[new_row][new_col] >= val and dfs(new_row, new_col):
                        # If so, we continue search on this neighbor.
                        return True
                return False

            return dfs(0, 0)

        left = 0
        right = min(grid[0][0], grid[-1][-1])

        while left < right:
            # Get the middle value between left and right boundaries.
            middle = (left + right + 1) // 2

            # Check if we can find a path with value = middle, and cut
            # the search space by half.
            if path_exists(middle):
                left = middle
            else:
                right = middle - 1

        # Once the left and right boundaries coincide, we find the target value,
        # that is, the maximum value of a path.
        return left

class Solution4:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        # 4 directions to a cell's possible neighbors.
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        heap = []
        ans = grid[0][0]

        # Initalize the status of all the cells as 0 (unvisited).
        visited = [[False] * C for _ in range(R)]

        # Put the top-left cell to the priority queue and mark it as True (visited).
        # Notice that we save the negative number of cell's value, thus we can always
        # pop out the cell with the maximum value using a min-heap data structure.
        heapq.heappush(heap, (-grid[0][0], 0, 0))
        visited[0][0] = True

        # While the priority queue is not empty.
        while heap:
            # Pop the cell with the largest value.
            cur_val, cur_row, cur_col = heapq.heappop(heap)

            # Update the minimum value we have visited so far.
            ans = min(ans, grid[cur_row][cur_col])

            # If we reach the bottom-right cell, stop the iteration.
            if cur_row == R - 1 and cur_col == C - 1:
                break
            for d_row, d_col in dirs:
                new_row = cur_row + d_row
                new_col = cur_col + d_col

                # Check if the current cell has any unvisited neighbors.
                if (
                    0 <= new_row < R
                    and 0 <= new_col < C
                    and not visited[new_row][new_col]
                ):
                    # If so, we put this neighbor to the priority queue
                    # and mark it as True (visited).
                    heapq.heappush(
                        heap, (-grid[new_row][new_col], new_row, new_col)
                    )
                    visited[new_row][new_col] = True

        # Return the minimum value we have seen, which is the value of this path.
        return ans

# Approach 5: Union Find
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # Find the root of x.
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        # Union the roots of x and y.
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    root[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    root[root_x] = root_y
                else:
                    root[root_y] = root_x
                    rank[root_x] += 1

        R = len(grid)
        C = len(grid[0])

        # 4 directions to a cell's possible neighbors.
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Intialize the rank of all the cells.
        rank = [1] * (R * C)

        # Intialize the root of all the cells.
        root = list(range(R * C))

        # Mark all the cells as false (unvisited).
        visited = [[False] * C for _ in range(R)]

        # Sort all the cells by values from large to small.
        vals = [(row, col) for row in range(R) for col in range(C)]
        vals.sort(key=lambda x: grid[x[0]][x[1]], reverse=True)

        # Iteration over the sorted cells.
        for cur_row, cur_col in vals:
            cur_pos = cur_row * C + cur_col

            # Mark the current cell as true (visited).
            visited[cur_row][cur_col] = True
            for d_row, d_col in dirs:
                new_row = cur_row + d_row
                new_col = cur_col + d_col
                new_pos = new_row * C + new_col

                # Check if the current cell has any unvisited neighbors with value larger
                # than or equal to val.
                if (
                    0 <= new_row < R
                    and 0 <= new_col < C
                    and visited[new_row][new_col]
                ):
                    # If so, we connect the current cell with this neighbor.
                    union(cur_pos, new_pos)

            # Check if the top-left cell is connected with the bottom-right cell.
            if find(0) == find(R * C - 1):
                # If so, return the value of the current cell.
                return grid[cur_row][cur_col]
        return -1