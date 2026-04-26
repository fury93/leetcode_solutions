class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxSub, curSub = 1, 1
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                curSub = 1
            else:
                curSub += 1
            maxSub = max(maxSub, curSub)
        
        return maxSub