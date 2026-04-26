class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = []
        for i in range(0, len(s), k):
            sm = 0
            for j in range(i, i + k):
                sm += ord(s[j]) - 97
            res.append(chr(97 + sm % 26))

        return ''.join(res)