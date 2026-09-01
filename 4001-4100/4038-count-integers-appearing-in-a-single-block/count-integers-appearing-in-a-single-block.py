class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        blocks = defaultdict(int)
        for d, _ in groupby(nums):
            blocks[d] += 1
        
        return sum(v == 1 for v in blocks.values())