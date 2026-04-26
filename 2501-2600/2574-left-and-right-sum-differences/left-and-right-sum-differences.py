class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rSum, lSum = sum(nums), 0
        for i, n in enumerate(nums):
            rSum-=n
            nums[i] = abs(rSum - lSum)
            lSum+=n
        
        return nums