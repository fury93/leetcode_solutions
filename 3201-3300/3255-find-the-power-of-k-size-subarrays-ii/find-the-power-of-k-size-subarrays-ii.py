class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums

        res, conseq = [-1] * (len(nums) - k + 1), 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] + 1:
                conseq += 1
            else:
                conseq = 1

            if conseq >= k:
                res[i - k + 1] = nums[i]

        return res