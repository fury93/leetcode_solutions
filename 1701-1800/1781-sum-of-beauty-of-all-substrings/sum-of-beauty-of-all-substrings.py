class Solution:
    def beautySum(self, s: str) -> int:
        res, L = 0, len(s)
        nums = [ord(ch) - 97 for ch in s]
        for i in range(L):
            freq = [0] * 26
            for j in range(i, L):
                freq[nums[j]] += 1
                
                mx, mn  = 0, L
                for fr in freq:
                    if fr > 0:
                        mx = max(mx, fr)
                        mn = min(mn, fr)
                res += mx - mn
                
        return res

    def beautySum2(self, s: str) -> int:
        res, freq = 0, defaultdict(int)
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                freq[ord(s[j]) - 97] += 1
                vals = [val for val in freq if val > 0]
                res += max(vals) - min(vals)
        return res
