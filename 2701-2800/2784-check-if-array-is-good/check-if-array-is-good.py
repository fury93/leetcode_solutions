class Solution:
    def isGood(self, nums: List[int]) -> bool:
        L = len(nums) - 1
        return sorted(nums) == list(range(1, L+1)) + [L]     