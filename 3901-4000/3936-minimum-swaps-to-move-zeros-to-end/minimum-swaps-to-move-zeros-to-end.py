class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        zall = nums.count(0)
        zend = nums[-zall:].count(0)
        return zall - zend
