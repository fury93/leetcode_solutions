class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i, n in enumerate(nums):
            left = bisect_left(nums, lower - n, i + 1)
            right = bisect_right(nums, upper - n, i + 1)
            res += right - left

        return res