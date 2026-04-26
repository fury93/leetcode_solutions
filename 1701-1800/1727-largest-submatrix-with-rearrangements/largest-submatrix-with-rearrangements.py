class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        res = 0
        for i, r in enumerate(matrix):
            for j, c in enumerate(r):
                if i and c:
                    matrix[i][j] += matrix[i-1][j]
            for k, v in enumerate(sorted(r)[::-1], 1):
                res = max(res, k*v)
        return res