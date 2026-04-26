class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        nums_s = set(nums)
        start = max(1, sum(nums) // len(nums) + 1)
        for i in range(start, 102):
            if i not in nums_s: break
        return i