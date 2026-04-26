class Solution:
    def largestEvenSum(self, A: List[int], k: int) -> int:
        A.sort(reverse = True)
        n = len(A)
        res = sum(A[:k])
        
        if res % 2 == 0: return res
        
        odd, even = 10 ** 6, 10 ** 6
        
        for i in range(k):
            if A[i] % 2: odd = min(odd, A[i])
            else: even = min(even, A[i])
                
        ans = -1
        for i in range(k, n):
            if A[i] % 2 and even != 10 ** 6:
                ans = max(ans, res - even + A[i])
            if A[i] % 2 == 0 and odd != 10 ** 6:
                ans = max(ans, res - odd + A[i])
        
        return ans