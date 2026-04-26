class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for key, val in cnt.items():
            res = max(res, val + cnt.get(key+1, -val))
        return res