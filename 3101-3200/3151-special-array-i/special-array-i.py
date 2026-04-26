class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all(a & 1 != b & 1 for a, b in pairwise(nums))