class Solution:
    def findFarmland2(self, land: List[List[int]]) -> List[List[int]]:
        res, ROWS, COLS = [], len(land), len(land[0])
        
        for r, c in product(range(ROWS), range(COLS)):
            if land[r][c] == 1:
                # it's part of processed land, we need to find only top-left coordinats
                if (r >= 1 and land[r-1][c] == 1) or (c >= 1 and land[r][c-1] == 1): continue
                r2, c2 = r, c
                while r2 < ROWS and land[r2][c] == 1:
                    r2 += 1
                while c2 < COLS and land[r][c2] == 1:
                    c2 += 1
                res.append([r, c, r2-1, c2-1])
        
        return res
    
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res, ROWS, COLS = [], len(land), len(land[0])
        
        for r in range(ROWS):
            c = 0
            while c < COLS:
                if land[r][c] == 1:
                    r2, c2 = r, c
                    # find width of the farmland (top-right coordinats)
                    while c2 < COLS and land[r][c2] == 1:
                        c2 += 1
                    width = c2 - c + 1
                    # set mark in the left border about farmland width
                    while r2 < ROWS and land[r2][c] == 1:
                        land[r2][c] = width
                        r2 += 1
                    res.append([r, c, r2-1, c2-1])
                
                if land[r][c] > 1: #make jump
                    c = c + land[r][c]
                else:
                    c += 1
        
        return res

    def findFarmland3(self, land: List[List[int]]) -> List[List[int]]:
        res, ROWS, COLS = [], len(land), len(land[0])
        
        def dfs(r, c):
            maxRightDown = (r, c)
            land[r][c] = 0
            for dr, dc in [(0, 1), (1, 0)]:
                rr, cc = r + dr, c + dc
                if rr < ROWS and cc < COLS and land[rr][cc] == 1:
                    maxRightDown = max(dfs(rr, cc), maxRightDown)
            return maxRightDown 

        for r, c in product(range(ROWS), range(COLS)):
            if land[r][c] == 1:
                r2, c2 = dfs(r, c)
                res.append([r, c, r2, c2])
        
        return res