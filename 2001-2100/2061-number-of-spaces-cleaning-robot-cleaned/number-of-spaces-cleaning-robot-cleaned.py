class Solution:
    # BFS
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        DIRECTIONS = (0, 1, 0, -1, 0)
        rows, cols = len(room), len(room[0])
        visited = [[0] * cols for _ in range(rows)]
        cleaned = 0

        queue = deque([(0, 0, 0)])
        while queue:
            row, col, direction = queue.popleft()

            # If the robot hasn't cleaned this space yet, increment cleaned
            if visited[row][col] == 0:
                cleaned += 1

            # Mark the space as visited facing this direction
            visited[row][col] |= 1 << direction

            for d in range(4):
                # Get the next direction and coordinates for the next space
                next_dir = (direction + d) % 4
                next_row = row + DIRECTIONS[next_dir]
                next_col = col + DIRECTIONS[next_dir + 1]

                # Clean the next space if it's empty and in the room
                if (
                    0 <= next_row < len(room)
                    and 0 <= next_col < len(room[0])
                    and room[next_row][next_col] == 0
                ):
                    # If we already visited the next space facing the next
                    # direction, return the number of spaces cleaned
                    if visited[next_row][next_col] >> next_dir & 1:
                        return cleaned
                    else:
                        queue.append((next_row, next_col, next_dir))
                        break

        return cleaned

    def numberOfCleanRooms2(self, room: List[List[int]]) -> int:
        res, row, col, dx, dy, R, C = 0, 0, 0, 1, 0, len(room), len(room[0])

        while True:
            if room[y][x] >= 1:
                break
            
            res += 1
            room[y][x] = (2, (dx, dy))
            for _ in range(4):
                xx, yy = x + dx, y + dy
                if (xx < 0 or xx >= C or yy < 0 or yy >= R) or room[yy][xx] == 1:
                    dx, dy = -dy, dx
                elif room[yy][xx] == 0:
                    x, y = xx, yy
                    break
        
        return res