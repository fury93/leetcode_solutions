# Time: O(N*log10(M)), where M - max number
# SpaceЖ O(log10(M))
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            digSum = sum(map(int, str(n)))
            if digSum == i: return i
        return -1