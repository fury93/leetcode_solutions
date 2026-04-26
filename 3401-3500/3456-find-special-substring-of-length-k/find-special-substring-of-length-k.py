class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                if cnt == k: return True
                cnt = 1

        return cnt == k