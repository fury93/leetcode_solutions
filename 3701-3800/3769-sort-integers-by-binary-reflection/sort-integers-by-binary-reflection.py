class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        reversedBin = [int(f"{n:b}"[::-1], 2) for n in nums]
        return [pair[1] for pair in sorted(zip(reversedBin, nums))]