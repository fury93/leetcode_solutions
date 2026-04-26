class Solution:
    def canDivideIntoSubsequences(self, A, K):
        return len(A) >= K * max(collections.Counter(A).values())