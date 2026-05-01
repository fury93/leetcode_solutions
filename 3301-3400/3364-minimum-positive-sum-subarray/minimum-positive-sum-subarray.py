class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        prefix = list(accumulate(nums, initial = 0))
        res, ln = inf, len(nums)
        for k in range(l, r+1):
            for i in range(ln - k + 1):
                sm = prefix[i + k] - prefix[i]
                if sm > 0:
                    res = min(res, sm)

        return -1 if res == inf else res