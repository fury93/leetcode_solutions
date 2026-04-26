class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(0, max(accumulate(gain)))
        
        prefix, res = 0, 0
        for g in gain:
            prefix += g
            res = max(res, prefix)
        return res