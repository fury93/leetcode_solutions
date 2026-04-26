class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        n = len(s)
        res = sorted(ch for ch in s)
        i = j = (n+1)//2
        while j < n and (res[j] == res[i]):
            j += 1 
        while res[i] == res[n-i-1]:
            if j == n:
                return "-1"
            res[i] , res[j] = res[j], res[i]
            i += 1
            j += 1
        return "".join(res)