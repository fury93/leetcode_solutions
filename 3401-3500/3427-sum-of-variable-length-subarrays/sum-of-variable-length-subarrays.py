class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums, initial = 0))
        res = 0

        for i, n in enumerate(nums):
            start = max(0, i - n)
            res += prefix[i+1] - prefix[start]

        return res