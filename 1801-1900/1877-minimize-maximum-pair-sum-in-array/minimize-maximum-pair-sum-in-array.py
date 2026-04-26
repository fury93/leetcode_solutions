class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        l, r, res = 0, len(nums)-1, 0
        nums.sort()
        while l < r:
            res = max(res, nums[l] + nums[r])
            l += 1
            r -= 1
        
        return res