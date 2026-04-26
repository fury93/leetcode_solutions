class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def calculateMaxHeight(colors):
            res, rowSize, i = 0, 1, 0
            while colors[i] >= rowSize:
                res += 1
                colors[i] -= rowSize
                rowSize += 1
                i = i ^ 1

            return res

        return max(calculateMaxHeight([red, blue]), calculateMaxHeight([blue, red]))