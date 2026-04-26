class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        q, ROWS, COLS, EMPTY = deque(), len(rooms), len(rooms[0]), 2147483647

        for row, col in product(range(ROWS), range(COLS)):
            if rooms[row][col] == 0:
                q.append((row, col))
        
        while q:
            row, col = q.popleft()
            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # right, down, left, up
                nextRow, nextCol = row + dy, col + dx
                if (
                    0 <= nextRow < ROWS and 
                    0 <= nextCol < COLS and
                    rooms[nextRow][nextCol] == EMPTY
                ):
                    rooms[nextRow][nextCol] = rooms[row][col] + 1
                    q.append((nextRow, nextCol))