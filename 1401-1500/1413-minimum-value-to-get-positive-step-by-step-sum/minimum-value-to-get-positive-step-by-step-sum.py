class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix, res = 0, 0
        for n in nums:
            prefix += n
            if prefix < 1:
                res = min(res, prefix)
        return abs(res) + 1