class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        return max((k for k, v in Counter(nums).items() if v == 1), default = -1)