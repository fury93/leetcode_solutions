from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle by modifying the board in-place.
        """
        # Initialize data structures to keep track of constraints
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Populate the constraint sets and identify empty cells
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    box_index = (i // 3) * 3 + (j // 3)
                    boxes[box_index].add(num)
                else:
                    empty_cells.append((i, j))

        def backtrack(index):
            # If all empty cells are filled, the puzzle is solved
            if index == len(empty_cells):
                return True

            # Select the next empty cell with the fewest possible candidates (MRV heuristic)
            min_candidates = 10
            min_index = index
            for k in range(index, len(empty_cells)):
                i, j = empty_cells[k]
                box_index = (i // 3) * 3 + (j // 3)
                possible = {'1','2','3','4','5','6','7','8','9'} - rows[i] - cols[j] - boxes[box_index]
                candidates = len(possible)
                if candidates < min_candidates:
                    min_candidates = candidates
                    min_index = k
                if min_candidates == 1:
                    break  # Can't get better than this

            # Swap to prioritize the cell with the fewest candidates
            empty_cells[index], empty_cells[min_index] = empty_cells[min_index], empty_cells[index]
            i, j = empty_cells[index]
            box_index = (i // 3) * 3 + (j // 3)
            possible_numbers = {'1','2','3','4','5','6','7','8','9'} - rows[i] - cols[j] - boxes[box_index]

            for num in possible_numbers:
                # Place the number
                board[i][j] = num
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

                # Recurse to fill in the next cell
                if backtrack(index + 1):
                    return True

                # Backtrack if placing num doesn't lead to a solution
                board[i][j] = '.'
                rows[i].remove(num)
                cols[j].remove(num)
                boxes[box_index].remove(num)

            # If no number can be placed in this cell, trigger backtracking
            return False

        backtrack(0)

        
class Solution1:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        blocks = [[False] * 9 for _ in range(9)]
        emptyCells = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    dig = int(board[i][j]) - 1
                    rows[i][dig] = cols[j][dig] = blocks[i//3 * 3 + j//3][dig] = True
                else:
                    emptyCells.append((i, j))

        def dfs():
            if not emptyCells: return True
            i, j = emptyCells.pop()
            
            for n in range(9):
                if not rows[i][n] and not cols[j][n] and not blocks[i//3*3 + j//3][n]:
                    board[i][j] = str(n+1)
                    rows[i][n] = cols[j][n] = blocks[i//3*3 + j//3][n] = True

                    if dfs(): return True
                    
                    board[i][j] = '.'
                    rows[i][n] = cols[j][n] =  blocks[i//3*3 + j//3][n] = False
            
            emptyCells.append((i, j))

        dfs()

class Solution2:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (
                d in rows[row]
                or d in columns[col]
                or d in boxes[box_index(row, col)]
            )

        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            """
            Remove a number that didn't lead to a solution
            """
            rows[row][d] -= 1
            columns[col][d] -= 1
            boxes[box_index(row, col)][d] -= 1
            if rows[row][d] == 0:
                del rows[row][d]
            if columns[col][d] == 0:
                del columns[col][d]
            if boxes[box_index(row, col)][d] == 0:
                del boxes[box_index(row, col)][d]
            board[row][col] = "."

        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion to continue to place numbers
            till the moment we have a solution
            """
            if col == N - 1 and row == N - 1:
                sudoku_solved[0] = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            """
            Backtracking
            """
            if board[row][col] == ".":
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        if sudoku_solved[0]:
                            return
                        remove_number(d, row, col)
            else:
                place_next_numbers(row, col)

        n = 3
        N = n * n
        box_index = lambda row, col: (row // n) * n + col // n

        rows = [defaultdict(int) for _ in range(N)]
        columns = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = [False]
        backtrack()