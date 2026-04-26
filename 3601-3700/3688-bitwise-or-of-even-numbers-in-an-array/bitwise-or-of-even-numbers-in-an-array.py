class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x | y, (n for n in nums if not n & 1), 0)