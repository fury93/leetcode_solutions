class Solution:
    def smallestNumber(self, n: int) -> str:
        if n == 1: return "1"
        digits = []
        for i in range(9, 1, -1):
            while n and n % i == 0:
                digits.append(str(i))
                n //= i
        if n > 1: return "-1"
        return "".join(digits[::-1])