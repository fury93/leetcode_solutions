class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        return sum(map(int, str(min(nums)))) & 1 ^ 1