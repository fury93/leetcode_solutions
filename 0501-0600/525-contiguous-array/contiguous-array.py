class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res, s, d = 0, 0, {0: -1}
        for i, n in enumerate(nums):
            s += 1 if n == 1 else -1
            res = max(res, i - d.setdefault(s, i))
        return res