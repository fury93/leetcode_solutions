class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = len(nums) * [1]
        
        prefix = 1
        for i, val in enumerate(nums):
            res[i] = prefix
            prefix *= val
        postfix = 1
        for i, val in reversed(list(enumerate(nums))):
            res[i] *= postfix
            postfix *= val

        return res