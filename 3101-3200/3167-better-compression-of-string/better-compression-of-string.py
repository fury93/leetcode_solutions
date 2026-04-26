class Solution:
    def betterCompression(self, s):
        count = Counter()
        c = [i for i, c in enumerate(s) if c.isalpha()] + [len(s)]
        for i, j in zip(c[:-1], c[1:]): count[s[i]] += int(s[i+1:j])
        return ''.join([c+str(count[c]) for c in sorted(count)])     