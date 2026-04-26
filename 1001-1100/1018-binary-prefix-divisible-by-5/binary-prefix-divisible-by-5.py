class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res, prev = [], 0
        for n in nums:
            cur = 2 * prev + n
            res.append(cur % 5 == 0)
            prev = cur
        return res