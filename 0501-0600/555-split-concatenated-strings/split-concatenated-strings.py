class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        strs = [s[::-1] if s[::-1] > s else s for s in strs]
        ans = ''.join(strs)
        for i, s in enumerate(strs):
            t = ''.join(strs[i + 1 :]) + ''.join(strs[:i])
            for j in range(len(s)):
                a = s[j:]
                b = s[:j]
                ans = max(ans, a + t + b)
                ans = max(ans, b[::-1] + t + a[::-1])
        return ans
        
class Solution2:
    def splitLoopedString(self, strs: List[str]) -> str:
        arr=[s if s>=s[::-1] else s[::-1] for s in strs]
        res=''
        for i,s in enumerate(arr):
            for s2 in [s,s[::-1]]:
                for j in range(len(s2)):
                    cur=s2[j:]+''.join(arr[i+1:]+arr[:i])+s2[:j]
                    res=max(res, cur)
        return res