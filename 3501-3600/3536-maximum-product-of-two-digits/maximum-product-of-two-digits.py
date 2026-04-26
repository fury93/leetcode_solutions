class Solution:
    def maxProduct(self, n: int) -> int:
        dig = sorted(str(n), reverse = True)
        return int(dig[0]) * int(dig[1])