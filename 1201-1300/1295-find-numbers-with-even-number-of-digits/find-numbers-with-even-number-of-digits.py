class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(not len(n) & 1 for n in map(str, nums))
        # return sum(1 for n in nums if len(str(n)) & 1 == 0)