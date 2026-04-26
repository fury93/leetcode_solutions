class Solution:
    def numberOfSubstrings(self, s, k):
        res, start, count = 0, 0, Counter()
        for end, c in enumerate(s):
            count[c] += 1
            while count[c] == k:
                res += len(s) - end
                count[s[start]] -= 1
                start += 1
        return res        