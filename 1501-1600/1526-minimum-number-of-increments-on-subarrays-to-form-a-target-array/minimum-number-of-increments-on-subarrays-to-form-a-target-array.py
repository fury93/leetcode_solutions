class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res, prev = 0, 0
        for n in target:
            res += max(n - prev, 0)
            prev = n
        
        return res