class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, ln = 0, 0
        for i in range(2, len(nums)):
            if nums[i] == nums[i-1] + nums[i-2]:
                ln += 1
                res = max(res, ln)
            else:
                ln = 0
            
        return res + 2