class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res, prev, seq = [], "", string.ascii_lowercase
        for ch in target:
            for i in range(ord(ch) - 96):
                s = prev + seq[i]
                res.append(s)
            prev = s

        return res