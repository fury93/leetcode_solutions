class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digits = list(map(int, str(n)))
        return sum(x**2 for x in digits) - sum(digits) >= 50