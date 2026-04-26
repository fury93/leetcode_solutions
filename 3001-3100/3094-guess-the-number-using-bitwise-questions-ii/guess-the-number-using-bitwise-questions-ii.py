# Definition of commonBits API.
# def commonBits(num: int) -> int:

class Solution:
    def findNumber(self) -> int:
        ans = 0
        baseline = commonBits(0)
        for i in range(30):
            b = 1 << i
            res = commonBits(b)
            if res > baseline:
                ans |= b
            baseline = res
        return ans

class Solution2:
    def findNumber(self):
        return reduce(lambda a, b: a | b,[1 << i  for i in range(30) if commonBits(1 << i) > commonBits(1 << i)])        