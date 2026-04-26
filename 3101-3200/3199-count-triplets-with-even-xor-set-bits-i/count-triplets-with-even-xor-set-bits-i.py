# 3215 https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/description/

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        (oddA, evenA), (oddB, evenB), (oddC, evenC) = self.cnts(a), self.cnts(b), self.cnts(c)
        return evenA*evenB*evenC + evenA*oddB*oddC + oddA*evenB*oddC + oddA*oddB*evenC
        
    def cnts(self, arr: List[int]) -> (int, int):
        odd = sum(num.bit_count() & 1 for num in arr)
        even = len(arr) - odd
        return odd, even