class Solution:
    def tourOfKnight(self, m, n, r, c):
        # Possible knight moves: (row, column) pairs
        knight_moves = [
            (-1, -2),
            (-2, -1),
            (-1, 2),
            (-2, 1),
            (1, -2),
            (2, -1),
            (1, 2),
            (2, 1),
        ]
        chessboard = [[0] * n for _ in range(m)]

        chessboard[r][c] = -1

        def _solve_knights_tour(current_row, current_col, move_count):
            # Base case: if all cells have been visited, we've found a solution
            if move_count == m * n:
                return True

            # Get and sort possible next moves based on Warnsdorff's rule
            next_moves = _get_next_moves_warnsdorff(current_row, current_col)

            # Try each possible move
            for _, move_index in next_moves:
                next_row, next_col = (
                    current_row + knight_moves[move_index][0],
                    current_col + knight_moves[move_index][1],
                )

                # Check if the move is valid
                if not _is_valid_move(next_row, next_col):
                    continue

                # Mark the move as visited
                chessboard[next_row][next_col] = move_count

                # Recursively try to solve from this new position
                if _solve_knights_tour(next_row, next_col, move_count + 1):
                    return True

                # If the move doesn't lead to a solution, backtrack
                chessboard[next_row][next_col] = 0

            return False  # No solution found from this position

        # Implement Warnsdorff's rule: prefer moves with fewer onward moves
        def _get_next_moves_warnsdorff(row, col):
            next_moves = []
            for idx in range(8):
                next_row, next_col = (
                    row + knight_moves[idx][0],
                    col + knight_moves[idx][1],
                )
                accessibility_score = sum(
                    _is_valid_move(next_row + move[0], next_col + move[1])
                    for move in knight_moves
                )
                next_moves.append((accessibility_score, idx))

            # Sort moves based on accessibility (fewer accessible squares first)
            return sorted(next_moves)

        # Check if the move is valid
        def _is_valid_move(row, col):
            return 0 <= row < m and 0 <= col < n and chessboard[row][col] == 0

        _solve_knights_tour(r, c, 1)

        # Reset the starting position to 0
        chessboard[r][c] = 0

        return chessboard
        
class Solution2:
    def tourOfKnight(self, m, n, r, c):
        # Precompute possible knight moves
        moves = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ]

        def _is_valid_move(to_row, to_col):
            return (
                0 <= to_row < m
                and 0 <= to_col < n
                and chessboard[to_row][to_col] == 0
            )

        def _solve_knights_tour(current_row, current_col, move_count):
            # Base case: if all cells have been visited, we've found a solution
            if move_count == m * n:
                return True

            # Try all possible knight moves
            for move_r, move_c in moves:
                new_row, new_col = current_row + move_r, current_col + move_c
                # Check if the move is valid
                if _is_valid_move(new_row, new_col):
                    chessboard[new_row][new_col] = move_count

                    # Recursively try to solve from this new position
                    if _solve_knights_tour(new_row, new_col, move_count + 1):
                        return True

                    # If the move doesn't lead to a solution, backtrack
                    chessboard[new_row][new_col] = 0

            # If no solution is found from the current position
            return False

        chessboard = [[0] * n for _ in range(m)]

        chessboard[r][c] = -1

        # Start the recursive solving process
        _solve_knights_tour(r, c, 1)

        chessboard[r][c] = 0

        return chessboard

class Solution3:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        board = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(i: int, j: int, k: int) -> bool:
            if k == m * n: return True
            for x, y in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
                if 0 <= i + x < m and 0 <= j + y < n and board[i + x][j + y] == -1:
                    board[i + x][j + y] = k
                    if dfs(i + x, j + y, k + 1): return True
                    board[i + x][j + y] = -1
            return False
        
        board[r][c] = 0
        dfs(r, c, 1)
        return board