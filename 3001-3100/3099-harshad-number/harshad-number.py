class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sm = sum(map(int, str(x)))
        return sm if x % sm == 0 else - 1