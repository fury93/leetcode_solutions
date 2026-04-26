class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res, ln = 0, len(nums)
        for i, n in enumerate(nums):
            isGood = True
            if i - k >= 0 and nums[i-k] >= n:
                isGood = False
            
            if isGood and i + k < ln and nums[i+k] >= n:
                isGood = False
            
            if isGood:
                res += n

        return res