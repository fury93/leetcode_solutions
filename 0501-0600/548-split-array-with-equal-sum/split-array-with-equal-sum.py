class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        s = [0] * (n + 1)
        for i, v in enumerate(nums):
            s[i + 1] = s[i] + v
        for j in range(3, n - 3):
            seen = set()
            for i in range(1, j - 1):
                if s[i] == s[j] - s[i + 1]:
                    seen.add(s[i])
            for k in range(j + 2, n - 1):
                if s[n] - s[k + 1] == s[k] - s[j + 1] and s[n] - s[k + 1] in seen:
                    return True
        return False
        
class Solution3(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def split(A):
            total = sum(A)
            for i in range(1, len(A)): A[i] += A[i-1]
            return {A[i-1] for i in range(1, len(A)-1) if A[i-1] == total - A[i]}
            
        return len(nums) > 6 and any(split(nums[:j]) & split(nums[j+1:]) \
                             for j in range(3, len(nums)-3))

class Solution2:
    def splitArray(self, A):
        P = [0]
        for x in A: P.append(P[-1] + x)
        
        N = len(A)
        Pinv = collections.defaultdict(list)
        for i, u in enumerate(P):
            Pinv[u].append(i)
            
        for j in range(1, N-1):
            for k in range(j+1, N-1):
                for i in Pinv[P[-1] - P[k+1]]:
                    if i >= j: break
                    if P[i] == P[j] - P[i+1] == P[k] - P[j+1]:
                        return True
        return False
        