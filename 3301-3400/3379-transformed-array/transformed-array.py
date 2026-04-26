class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [nums[(n + i) % len(nums)] for i, n in enumerate(nums)]
    
    def constructTransformedArray2(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        res = [None] * ln

        for i, n in enumerate(nums):
            if n > 0:
                res[i] = nums[(i + n) % ln]
            elif n < 0:
                res[i] = nums[(i - abs(n) + ln) % ln]
            else:
                res[i] = n

        return res