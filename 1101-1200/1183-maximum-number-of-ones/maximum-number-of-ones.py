class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        res = []
        for i in range(sideLength):
            for j in range(sideLength):
                res += [((width - i - 1) // sideLength + 1) * ((height - j - 1) // sideLength + 1)]
        res = sorted(res,reverse = True)
        return sum(res[:maxOnes])