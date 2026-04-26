class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d, s = {0: -1}, 0
        for i, n in enumerate(nums):
            s = (s + n) %k
            j = d.setdefault(s, i)
            if i - j >= 2: return True
        return False
