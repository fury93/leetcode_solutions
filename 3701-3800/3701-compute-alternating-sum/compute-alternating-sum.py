class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even = odd = 0

        for i, n in enumerate(nums):
            if i & 1:
                odd += n
            else:
                 even += n

        return even - odd