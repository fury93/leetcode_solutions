class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res, maxab, maxa = 0, 0, 0
        for c in nums:
            res = max(res, maxab * c)
            maxa = max(maxa, c)
            maxab = max(maxab, maxa - c)
        return res

