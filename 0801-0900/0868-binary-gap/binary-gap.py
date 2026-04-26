class Solution:
    def binaryGap(self, n: int) -> int:
        pos = [i for i, n in enumerate(f'{n:b}') if n == '1']
        return max((b-a for a, b in pairwise(pos)), default=0)