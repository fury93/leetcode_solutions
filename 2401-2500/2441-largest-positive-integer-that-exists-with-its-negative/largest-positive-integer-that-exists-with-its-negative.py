class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res, nums_s = 0, set(nums)
        for n in nums:
            if n > 0 and -n in nums_s and n > res:
                res = n
        return res if res > 0 else - 1