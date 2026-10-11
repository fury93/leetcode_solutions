class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        L = len(nums)
        res = 0
        for i, n in enumerate(nums, start=1):
            if L % i == 0:
                res += n*n
        return res