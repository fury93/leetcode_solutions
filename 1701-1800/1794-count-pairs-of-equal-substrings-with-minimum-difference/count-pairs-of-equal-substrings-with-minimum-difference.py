class Solution:
    def countQuadruples(self, f: str, s: str) -> int:
        l = {}
        r = {}
        for i in range(len(f)):
            if f[i] not in l:
                l[f[i]] = i
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in r:
                r[s[i]] = i
        res = defaultdict(int)
        for i in range(26):
            c = chr(ord('a') + i)
            if c in l and c in r:
                v = l[c] - r[c]
                res[v] += 1
        if not res: return 0
        mi = min(res.keys())
        return res[mi]

        
class Solution2:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        
        # 1. Find the first occurrence of each character in firstString.
        first = {}
        for j, char in enumerate(firstString):
            first.setdefault(char, j)
            
        # 2. Find the last occurrence of each character in secondString.
        last = {}            
        for a, char in enumerate(secondString):
            last[char] = a
        
        # 3. Find the value of (j - a) for characters that appear in both strings.
        diff_ja = defaultdict(list)
        overlap = set(firstString) & set(secondString)
        for char in overlap:
            diff_ja[first[char] - last[char]].append(char)
        
        # 4. Return the number of characters that share the minimum (j - a) value.
        mini = min(diff_ja.keys() or [0])
        return len(diff_ja[mini])