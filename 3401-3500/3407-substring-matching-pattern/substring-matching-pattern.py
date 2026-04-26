class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        s1, s2 = p.split('*')
        start1, start2 = s.find(s1), s.rfind(s2)
        return start1 > -1 and start1 + len(s1) <= start2 
        