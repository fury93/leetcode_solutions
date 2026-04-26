class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDif, l, r = -1, 0, 0

        while r < len(nums):
            dif = nums[r] - nums[l]
            if dif > 0:
                maxDif = max(maxDif, dif)
            else:
                l = r
            r +=1
        
        return maxDif