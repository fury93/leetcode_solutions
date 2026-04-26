class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        jump = [[0 for _ in range(10)] for _ in range(10)]

        # Initialize the jump over numbers for all valid jumps
        jump[1][3] = jump[3][1] = 2
        jump[4][6] = jump[6][4] = 5
        jump[7][9] = jump[9][7] = 8
        jump[1][7] = jump[7][1] = 4
        jump[2][8] = jump[8][2] = 5
        jump[3][9] = jump[9][3] = 6
        jump[1][9] = jump[9][1] = jump[3][7] = jump[7][3] = 5

        visited_numbers = [False] * 10
        total_patterns = 0

        # Count patterns starting from corner numbers (1, 3, 7, 9) and multiply by 4 due to symmetry
        total_patterns += (
            self._count_patterns_from_number(1, 1, m, n, jump, visited_numbers)
            * 4
        )

        # Count patterns starting from edge numbers (2, 4, 6, 8) and multiply by 4 due to symmetry
        total_patterns += (
            self._count_patterns_from_number(2, 1, m, n, jump, visited_numbers)
            * 4
        )

        # Count patterns starting from the center number (5)
        total_patterns += self._count_patterns_from_number(
            5, 1, m, n, jump, visited_numbers
        )

        return total_patterns

    def _count_patterns_from_number(
        self,
        current_number: int,
        current_length: int,
        min_length: int,
        max_length: int,
        jump: list,
        visited_numbers: list,
    ) -> int:
        # Base case: if current pattern length exceeds max_length, stop exploring
        if current_length > max_length:
            return 0

        valid_patterns = 0
        # If current pattern length is within the valid range, count it
        if current_length >= min_length:
            valid_patterns += 1

        visited_numbers[current_number] = True

        # Explore all possible next numbers
        for next_number in range(1, 10):
            jump_over_number = jump[current_number][next_number]
            # Check if the next number is unvisited and either:
            # 1. There's no number to jump over, or
            # 2. The number to jump over has been visited
            if not visited_numbers[next_number] and (
                jump_over_number == 0 or visited_numbers[jump_over_number]
            ):
                valid_patterns += self._count_patterns_from_number(
                    next_number,
                    current_length + 1,
                    min_length,
                    max_length,
                    jump,
                    visited_numbers,
                )

        # Backtrack: unmark the current number before returning
        visited_numbers[current_number] = False

        return valid_patterns

# Approach 1: Backtracking
class Solution1:
    # All possible single-step moves on the lock pattern grid
    # Each tuple represents a move as (row change, column change)
    SINGLE_STEP_MOVES = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),  # Adjacent moves (right, left, down, up)
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1),  # Diagonal moves
        (-2, 1),
        (-2, -1),
        (2, 1),
        (2, -1),  # Extended moves (knight-like moves)
        (1, -2),
        (-1, -2),
        (1, 2),
        (-1, 2),
    ]

    # Moves that require a dot to be visited in between
    # These moves "jump" over a dot, which must have been previously visited
    SKIP_DOT_MOVES = [
        (0, 2),
        (0, -2),
        (2, 0),
        (-2, 0),  # Straight skip moves (e.g., 1 to 3, 4 to 6)
        (-2, -2),
        (2, 2),
        (2, -2),
        (-2, 2),  # Diagonal skip moves (e.g., 1 to 9, 3 to 7)
    ]

    def numberOfPatterns(self, m: int, n: int) -> int:
        total_patterns = 0
        # Start from each of the 9 dots on the grid
        for row in range(3):
            for col in range(3):
                visited_dots = [[False for _ in range(3)] for _ in range(3)]
                # Count patterns starting from this dot
                total_patterns += self._count_patterns_from_dot(
                    m, n, 1, row, col, visited_dots
                )
        return total_patterns

    def _count_patterns_from_dot(
        self, m, n, current_length, current_row, current_col, visited_dots
    ):
        # Base case: if current pattern length exceeds n, stop exploring
        if current_length > n:
            return 0

        valid_patterns = 0
        # If current pattern length is within the valid range, count it
        if current_length >= m:
            valid_patterns += 1

        # Mark current dot as visited
        visited_dots[current_row][current_col] = True

        # Explore all single-step moves
        for move in self.SINGLE_STEP_MOVES:
            new_row = current_row + move[0]
            new_col = current_col + move[1]
            if self._is_valid_move(new_row, new_col, visited_dots):
                # Recursively count patterns from the new position
                valid_patterns += self._count_patterns_from_dot(
                    m, n, current_length + 1, new_row, new_col, visited_dots
                )

        # Explore all skip-dot moves
        for move in self.SKIP_DOT_MOVES:
            new_row = current_row + move[0]
            new_col = current_col + move[1]
            if self._is_valid_move(new_row, new_col, visited_dots):
                # Check if the middle dot has been visited
                middle_row = current_row + move[0] // 2
                middle_col = current_col + move[1] // 2
                if visited_dots[middle_row][middle_col]:
                    # If middle dot is visited, this move is valid
                    valid_patterns += self._count_patterns_from_dot(
                        m, n, current_length + 1, new_row, new_col, visited_dots
                    )

        # Backtrack: unmark the current dot before returning
        visited_dots[current_row][current_col] = False
        return valid_patterns

    def _is_valid_move(self, row, col, visited_dots):
        # A move is valid if it's within the grid and the dot hasn't been visited
        return 0 <= row < 3 and 0 <= col < 3 and not visited_dots[row][col]

# Approach 3: Memoization
class Solution3:
    def numberOfPatterns(self, m: int, n: int) -> int:
        jump = [[0] * 10 for _ in range(10)]

        # Initialize the jump over numbers for all valid jumps
        jump[1][3] = jump[3][1] = 2
        jump[4][6] = jump[6][4] = 5
        jump[7][9] = jump[9][7] = 8
        jump[1][7] = jump[7][1] = 4
        jump[2][8] = jump[8][2] = 5
        jump[3][9] = jump[9][3] = 6
        jump[1][9] = jump[9][1] = jump[3][7] = jump[7][3] = 5

        visited_numbers = 0
        total_patterns = 0
        dp = [[-1] * (1 << 10) for _ in range(10)]

        # Count patterns starting from corner numbers (1, 3, 7, 9) and multiply by 4 due to symmetry
        total_patterns += (
            self._count_patterns_from_number(
                1, 1, m, n, jump, visited_numbers, dp
            )
            * 4
        )

        # Count patterns starting from edge numbers (2, 4, 6, 8) and multiply by 4 due to symmetry
        total_patterns += (
            self._count_patterns_from_number(
                2, 1, m, n, jump, visited_numbers, dp
            )
            * 4
        )

        # Count patterns starting from the center number (5)
        total_patterns += self._count_patterns_from_number(
            5, 1, m, n, jump, visited_numbers, dp
        )

        return total_patterns

    def _count_patterns_from_number(
        self,
        current_number: int,
        current_length: int,
        min_length: int,
        max_length: int,
        jump: list,
        visited_numbers: int,
        dp: list,
    ) -> int:
        # Base case: if current pattern length exceeds max_length, stop exploring
        if current_length > max_length:
            return 0

        if dp[current_number][visited_numbers] != -1:
            return dp[current_number][visited_numbers]

        valid_patterns = 0
        # If current pattern length is within the valid range, count it
        if current_length >= min_length:
            valid_patterns += 1

        visited_numbers = self._set_bit(visited_numbers, current_number)

        # Explore all possible next numbers
        for next_number in range(1, 10):
            jump_over_number = jump[current_number][next_number]
            # Check if the next number is unvisited and either:
            # 1. There's no number to jump over, or
            # 2. The number to jump over has been visited
            if not self._is_set(visited_numbers, next_number) and (
                jump_over_number == 0
                or self._is_set(visited_numbers, jump_over_number)
            ):
                valid_patterns += self._count_patterns_from_number(
                    next_number,
                    current_length + 1,
                    min_length,
                    max_length,
                    jump,
                    visited_numbers,
                    dp,
                )

        # Backtrack: unmark the current number before returning
        visited_numbers = self._clear_bit(visited_numbers, current_number)

        dp[current_number][visited_numbers] = valid_patterns
        return valid_patterns

    def _set_bit(self, num: int, position: int) -> int:
        num |= 1 << (position - 1)
        return num

    def _clear_bit(self, num: int, position: int) -> int:
        num ^= 1 << (position - 1)
        return num

    def _is_set(self, num: int, position: int) -> bool:
        bit_at_position = (num >> (position - 1)) & 1
        return bit_at_position == 1
