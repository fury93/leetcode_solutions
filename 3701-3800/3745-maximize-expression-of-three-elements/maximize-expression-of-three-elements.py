class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        snums = sorted(nums)
        return snums[-1] + snums[-2] - snums[0]