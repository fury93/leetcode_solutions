class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        return reduce(xor, chain(nums, set(nums)))
