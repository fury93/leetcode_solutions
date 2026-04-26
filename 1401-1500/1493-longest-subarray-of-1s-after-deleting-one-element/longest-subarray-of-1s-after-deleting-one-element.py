class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, l, prefix = 0, 0, 0
        for r, n in enumerate(nums):
            prefix += n
            if prefix < r - l:
                prefix -= nums[l]
                l += 1
        return r - l
        
    def longestSubarray2(self, nums: List[int]) -> int:
        res, l, prefix = 0, 0, 0
        for r, n in enumerate(nums):
            prefix += n
            while prefix < r-l:
                prefix -= nums[l]
                l += 1
            res = max(res, r-l)
        return res