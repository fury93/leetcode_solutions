class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(''.join('1' if c == '0' else '0' for c in f'{n:b}'), 2)