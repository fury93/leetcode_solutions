class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        cntNums = Counter(nums)
        cntFreq = Counter(cntNums.values())
        for n in nums:
            if cntFreq[cntNums[n]] == 1: return n
        return -1