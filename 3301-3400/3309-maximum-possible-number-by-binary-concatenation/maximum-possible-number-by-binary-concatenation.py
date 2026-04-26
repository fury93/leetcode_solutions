from itertools import permutations
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        bins = [f"{n:b}" for n in nums]
        bins.sort(key = lambda x: x*10, reverse=True)
        return int(''.join(bins), 2)

    def maxGoodNumber2(self, nums: List[int]) -> int:
        bins = [f"{n:b}" for n in nums]
        res = 0

        for perm in permutations(bins):
            val = int(''.join(perm), 2)
            res = max(res, val)
        
        return res