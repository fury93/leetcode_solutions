class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        res, l, seen = 0, 0, [-1] * 128
        for r, ch in enumerate(s):
            key = ord(ch)
            if seen[key] >= l:
                l = seen[key] + 1
            seen[key] = r
            res += r - l + 1
            
        return res
        
    # Not working approach, look later with test case "afiau"
    def numberOfSpecialSubstrings2(self, s: str) -> int:
        res, l, lastSeenPos = 0, 0, defaultdict(lambda: -1)

        # diapason [l:r) and number of substrings with len > 1 
        def addToResult(l, r):
                ln = r - l
                nonlocal res
                res += ln * (ln - 1) // 2

        for r, ch in enumerate(s):
            if lastSeenPos[ch] >= l: 
                addToResult(l, r)
                l = lastSeenPos[ch] + 1
            lastSeenPos[ch] = r
        
        addToResult(l, r + 1)

        return res + len(s)