class Solution(object):
    def solve(self, board):
        R, C = len(board), len(board[0])
        if R < 3 or C < 3: return
        CAPTURED, FREE, ESCAPED = 'X', 'O', 'E' 
        
        def dfs(board, row, col):
            if 0 <= row < R and 0 <= col < C and board[row][col] == FREE:
                board[row][col] = ESCAPED
                for diffRow, diffCol in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    dfs(board, row + diffRow, col + diffCol)
        
        # mark all regions (starts from the borders) that can't be captured like espaped
        for row, col in chain(product([0, R-1], range(C)), product(range(1, R-1), [0, C-1])):
            dfs(board, row, col) 
                 
        for row, col in product(range(R), range(C)):
            if board[row][col] == FREE:
                board[row][col] = CAPTURED
            elif board[row][col] == ESCAPED:
                board[row][col] = FREE
                
    