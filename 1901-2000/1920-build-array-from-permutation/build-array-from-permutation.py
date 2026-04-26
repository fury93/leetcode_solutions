class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            res.append(nums[n])

        return res