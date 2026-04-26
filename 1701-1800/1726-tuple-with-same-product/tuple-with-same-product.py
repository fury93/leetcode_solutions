class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res, d = 0, defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = nums[i] * nums[j]
                res += d[k]
                d[k] += 1
        return res * 8