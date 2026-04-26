class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        for n in range(k, 101, k):
            if n not in s:
                return n

        return n + k