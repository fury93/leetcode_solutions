class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()

        if len(s1) > len(s2):
            s1, s2 = s2, s1
        
        l = 0
        while l < len(s1) and s1[l] == s2[l]:
            l += 1
        
        r1, r2 = len(s1) - 1, len(s2) - 1
        while r1 >= l and s1[r1] == s2[r2]:
            r1 -= 1
            r2 -= 1
        
        return l > r1
