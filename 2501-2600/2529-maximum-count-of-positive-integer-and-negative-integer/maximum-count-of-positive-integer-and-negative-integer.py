class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l = bisect_left(nums, 0)
        r = bisect_right(nums, 0)
        return max(l, len(nums) - r)