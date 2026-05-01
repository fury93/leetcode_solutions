class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        maxLeft = [None] * len(nums)
        maxRight = [None] * len(nums)

        mx = 0
        for i in range(len(nums)):
            maxLeft[i] = mx
            mx = max(mx, nums[i])

        mx = 0
        for i in range(len(nums)-1, -1, -1):
            maxRight[i] = mx
            mx = max(mx, nums[i])

        return [n for i, n in enumerate(nums) if maxLeft[i] < n or n > maxRight[i]]
        