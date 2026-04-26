class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t): return self.isOneEditDistance(t, s) 
        
        if len(t) - len(s) > 1: return False
        
        isChanged, i, j = False, 0, 0
        while i < len(s):
            if s[i] == t[j]:
                i, j = i + 1, j + 1
            else:
                if isChanged: return False
                isChanged = True
                if len(s) == len(t):
                    i, j = i + 1, j + 1
                else:
                    j += 1

        return isChanged or len(s) < len(t)


    def isOneEditDistance2(self, s: str, t: str) -> bool:
        l1, l2 = len(s), len(t)
        if abs(l1 - l2) > 1: return False
        
        # mode {1: insert, -1: remove, 0: change}
        mode, i, j, isEdited = l2 - l1, 0, 0, False

        while i < l1 or j < l2:
            ss = s[i] if i < l1 else None
            tt = t[j] if j < l2 else None
            if ss == tt:
                i, j = i + 1, j + 1
            else:
                if isEdited: return False
                isEdited = True
                if mode == 1:
                    j += 1
                elif mode == -1:
                    i += 1
                else:
                    i, j = i + 1, j + 1
        
        return isEdited