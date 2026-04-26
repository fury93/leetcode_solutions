class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res, l = 0, 0
        pos = [-1] * (10**4 + 1)
        prefix = [0] * (len(nums) + 1)
        for r, n in enumerate(nums):
            prefix[r+1] = prefix[r] + n
            if pos[n] >= l:
                l = pos[n] + 1
            pos[n] = r
            res = max(res, prefix[r+1] - prefix[l])
        
        return res
