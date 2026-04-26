class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        R, C = len(seats), len(seats[0])
        
        matching = [[-1] * C for _ in range(R)]
        
        def dfs(node, seen):
            r, c = node
            for nr, nc in [[r-1,c-1], [r,c-1],[r,c+1],[r-1,c+1],[r+1,c-1],[r+1,c+1]]: # assume a virtual edge connecting students who can spy
                if 0 <= nr < R and 0 <= nc < C and seen[nr][nc] == False and seats[nr][nc] == '.':
                    seen[nr][nc] = True
                    if matching[nr][nc] == -1 or dfs(matching[nr][nc], seen):
                        matching[nr][nc] = (r,c)
                        return True
            return False
        
        def Hungarian():
            res = 0
            for c in range(0,C,2):
                for r in range(R):
                    if seats[r][c] == '.':
                        seen = [[False] * C for _ in range(R)]
                        if dfs((r,c), seen):
                            res += 1
            return res
        
        res = Hungarian()
                
        count = 0
        for r in range(R):
            for c in range(C):
                if seats[r][c] == '.':
                    count += 1
        return count - res 