class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        d1, d2 = [0]*26, [0]*26
        for c1, c2 in zip(s1, s2):
            d1[ord(c1)-97] += 1
            d2[ord(c2)-97] += 1
        
        superiority, break1, break2 = 0, True, True
        for i in range(26):
            superiority += d1[i] - d2[i]
            if superiority > 0: break2 = False
            elif superiority < 0: break1 = False
            
        return break1 or break2

    def checkIfCanBreak2(self, s1: str, s2: str) -> bool:
        def isBreak(str1, str2):
            for ch1, ch2 in zip(str1, str2):
                if ch1 < ch2: return False
            return True
        
        return isBreak(sorted(s1), sorted(s2)) \
            or isBreak(sorted(s2), sorted(s1))