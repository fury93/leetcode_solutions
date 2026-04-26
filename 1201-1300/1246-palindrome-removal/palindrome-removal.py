from functools import lru_cache
class Solution(object):
    def minimumMoves(self, A):
        @lru_cache(None)
        def dp(i, j):
            if i > j: return 0
            res = dp(i, j - 1) + 1
            if A[j] == A[j - 1]:
                res = min(res, dp(i, j - 2) + 1)
            for k in range(i, j - 1):
                if A[j] == A[k]:
                    res = min(res, dp(i, k - 1) + dp(k + 1, j - 1))
            return res
        return dp(0, len(A) - 1)