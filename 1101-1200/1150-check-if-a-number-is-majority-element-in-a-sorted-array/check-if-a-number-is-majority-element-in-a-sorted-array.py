class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return bisect_right(nums, target) - bisect.bisect_left(nums, target) >= len(nums)//2 + 1