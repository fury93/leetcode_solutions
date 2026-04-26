class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        for a, b in zip_longest(v1, v2, fillvalue = 0):
            if a > b: return 1
            elif a < b: return -1
        
        return 0