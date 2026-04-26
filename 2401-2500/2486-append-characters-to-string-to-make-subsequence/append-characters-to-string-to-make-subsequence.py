class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j, L = 0, len(t)
        for c in s:
            if c == t[j]:
                j += 1
            if j == L: break
        
        return L - j