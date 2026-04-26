class Solution:
    def numberOfSubmatrices(self, A: List[List[str]]) -> int:
        n, m = len(A), len(A[0])
        X = [[0] * (m + 1) for i in range(n + 1)]
        Y = [[0] * (m + 1) for i in range(n + 1)]
        res = 0
        for i in range(n):
            for j in range(m):
                X[i][j] = X[i-1][j] + X[i][j-1] - X[i-1][j-1] + (A[i][j] == 'X')
                Y[i][j] = Y[i-1][j] + Y[i][j-1] - Y[i-1][j-1] + (A[i][j] == 'Y')
                if X[i][j] == Y[i][j] > 0:
                    res += 1
        return res