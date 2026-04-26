class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res, black, l = len(blocks), 0, 0
        for r, b in enumerate(blocks):
            if b == 'B': black += 1
            if r + 1 < k: continue
            
            res = min(res, k - black)
            black -= blocks[r-k+1] == 'B'
        
        return res