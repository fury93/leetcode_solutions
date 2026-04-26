class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 10**5+1

        if k == 1: return 0

        for r in range(k-1, len(nums)):
            res = min(res, nums[r] - nums[r-k+1])
        
        return res
