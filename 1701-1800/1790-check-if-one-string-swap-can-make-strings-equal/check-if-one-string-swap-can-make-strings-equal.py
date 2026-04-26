class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        isSwapped, pos = False, None

        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if c1 != c2:
                if isSwapped:
                    return False
                if pos is None:
                    pos = i
                else:  
                    if s1[pos] == c2 and s2[pos] == c1:
                        isSwapped = True
                        pos = None
                    else:
                        return False
                    
        return pos is None
