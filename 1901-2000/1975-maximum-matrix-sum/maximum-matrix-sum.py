class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sm, minAbsVal, negativeCntIsOdd, ln = 0, math.inf, False, len(matrix)
        
        for i, j in product(range(ln), range(ln)):
            sm += abs(matrix[i][j])
            minAbsVal = min(minAbsVal, abs(matrix[i][j]))
            if matrix[i][j] < 0:
                negativeCntIsOdd = not negativeCntIsOdd

        if negativeCntIsOdd:
            sm -= minAbsVal * 2

        return sm
        