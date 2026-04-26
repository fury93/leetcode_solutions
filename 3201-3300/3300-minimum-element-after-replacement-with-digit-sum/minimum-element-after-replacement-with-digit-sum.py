class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(map(int, str(n))) for n in nums)