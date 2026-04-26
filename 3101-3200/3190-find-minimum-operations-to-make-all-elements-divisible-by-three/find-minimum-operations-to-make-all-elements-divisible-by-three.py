class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(n % 3 != 0 for n in nums)