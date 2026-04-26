from bisect import bisect
class Solution:
    def maxSubstringLength(self, s: str) -> int:
        n = len(s)
        cnt = defaultdict(list)
        for i, c in enumerate(s):
            cnt[c].append(i)
        # print(cnt)
        def valid(l, r, c1, c2):
            for c in cnt:
                if not( (c==c1 or c==c2) or (cnt[c][0] > l and cnt[c][-1] < r) or bisect(cnt[c], l) == bisect(cnt[c], r)):
                    return False
            return True
        ans = -1
        for c1 in cnt:
            s1, e1 = cnt[c1][0], cnt[c1][-1]
            for c2 in cnt:
                s2, e2 = cnt[c2][0], cnt[c2][-1]
                # print([s1,e1], [s2,e2])
                length = e2-s1 + 1
                if length < ans or length == n:
                    continue
                if c1 == c2 and valid(s1, e2, c1, c2):
                    ans = length
                if e1 > e2 or s1 > s2:
                    continue
                if valid(s1, e2, c1, c2):
                    ans = length
                # print(ans, left, right, c1, c2, length)
        return ans
                
                
class Solution2:
    def maxSubstringLength(self, s: str) -> int:
        cnts = Counter(s)
        
        prefix = [[0 for char in range(26)] for i in range(len(s)+1)]
        rMost = {}
        lMost = {}
        ans = 0
        for i in range(1, len(s)+1):
            char = s[i-1]
            if char not in lMost:
                lMost[char] = i
            rMost[char] = i
            prefix[i][ord(char) - ord("a")] += 1
            for freq in range(26):
                prefix[i][freq] += prefix[i-1][freq]
        
    
        for char in lMost:
            left = lMost[char]
            for c2 in rMost:
                right = rMost[c2]
                if (right == len(s) and left == 1) or (right < left):
                    continue
                valid = True
                for i, (rfreq, lfreq) in enumerate(zip(prefix[right], prefix[left-1])):
                    if rfreq-lfreq != 0 and rfreq-lfreq != cnts[chr(i + ord("a"))]:
                        valid = False
                        break
                if valid:
                    ans = max(ans, right-left+1)
        return ans if ans != 0 else -1