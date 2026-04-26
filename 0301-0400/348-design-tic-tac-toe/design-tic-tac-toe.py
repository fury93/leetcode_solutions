class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag1 = self.diag2 = 0 # diagonal1 - main, diagonal2 - secondary
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        # +1 for player1 ; -1 for player1 ; winner if abs(points) = n
        point = 1 if player == 1 else -1 
        self.rows[row] += point
        self.cols[col] += point
        
        if row == col:
            self.diag1 += point
        if row + col == self.size - 1:
            self.diag2 += point

        if any(abs(p) == self.size for p in (self.rows[row], self.cols[col], self.diag1, self.diag2)):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)