class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0
        for i, n in enumerate(nums):
            rightSum -=n
            if leftSum == rightSum:
                return i
            leftSum +=n
        return -1