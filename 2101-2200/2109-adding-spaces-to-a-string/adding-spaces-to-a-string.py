class Solution:
    def addSpaces2(self, s: str, spaces: List[int]) -> str:
        res, j = [], 0
        for i, n in enumerate(s):
            if j < len(spaces) and spaces[j] == i:
                res.append(' ')
                j += 1
            res.append(n)

        return ''.join(res)
    
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res =[]
        l = 0
        for r in spaces :
            res.append(s[l:r])
            l = r
        res.append(s[l:])
        return " ".join(res)