class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        for n in nums:
            if not n & 1 and cnt[n] == 1:
                return n
        return -1