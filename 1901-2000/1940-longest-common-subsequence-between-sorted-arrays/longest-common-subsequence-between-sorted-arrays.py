class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        res = set(arrays[0])
        for i in range(1, len(arrays)):
            res &= set(arrays[i])
        return sorted(res)