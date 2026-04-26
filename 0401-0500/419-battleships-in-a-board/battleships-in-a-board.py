class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res, R, C, SHIP, W = 0, len(board), len(board[0]), 'X', '.'
        for r, c in product(range(R), range(C)):
            if board[r][c] == SHIP:
                if (r == 0 or board[r-1][c] == W) and (c == 0 or board[r][c-1] == W):
                    res += 1
        return res

    def countBattleships2(self, board: List[List[str]]) -> int:
        res, R, C = 0, len(board), len(board[0])
        
        def dfs(x, y):
            for dx, dy in [(1, 0), (0, 1)]:
                xx, yy = x + dx, y + dy
                if 0 <= xx < R and 0 <= yy < C and board[xx][yy] == 'X':
                    board[xx][yy] = '.'
                    dfs(xx, yy)

        for x in range(R):
            for y in range(C):
                if board[x][y] == '.': continue
                res += 1
                dfs(x, y)
                
        return res