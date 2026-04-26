class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        br = defaultdict(int)
        for pos, rad in lights:
            br[pos-rad] += 1
            br[pos+rad+1] -= 1
        
        res, curBright, maxBright = 0, 0, -1
        for pos, diff in sorted(br.items()):
            curBright += diff
            if curBright > maxBright:
                maxBright = curBright
                res = pos
        
        return res
