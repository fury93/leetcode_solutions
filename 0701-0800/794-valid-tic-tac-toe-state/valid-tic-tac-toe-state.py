class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(x):
            if any(r[0] == r[1] == r[2] == x for r in board): return True
            if any(c[0] == c[1] == c[2] == x for c in zip(*board)): return True
            if board[0][0] == board[1][1] == board[2][2] == x: return True
            if board[0][2] == board[1][1] == board[2][0] == x: return True
        
        d = Counter(''.join(board))
        x, y = d['X'], d['O']
        if x < y or x > y + 1: return False
        if win('X') and x != y + 1: return False
        if win('O') and x != y: return False
        
        return True
            