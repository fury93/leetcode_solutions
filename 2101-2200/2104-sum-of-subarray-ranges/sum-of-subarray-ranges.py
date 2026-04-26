class Solution:
    def subArrayRanges(self, A):
        res = 0
        n = len(A)
        for i in range(n):
            l,r = A[i],A[i]
            for j in range(i, n):
                l = min(l, A[j])
                r = max(r, A[j])
                res += r - l
        return res