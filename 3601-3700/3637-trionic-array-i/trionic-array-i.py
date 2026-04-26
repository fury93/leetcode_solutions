class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        signs = [(b > a) - (a > b) for a, b in pairwise(nums)]
        return [1, -1, 1] == [sign for sign, _ in groupby(signs)]