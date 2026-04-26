class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return sum(a != b for a, b in pairwise(nums))