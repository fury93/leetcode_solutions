class Solution:
    def compressedString(self, word: str) -> str:
        res, i = [], 0
        while i < len(word):
            ch, cnt = word[i], 0
            while i < len(word) and word[i] == ch and cnt < 9:
                i += 1
                cnt += 1
            res.extend([str(cnt), ch])
        
        return ''.join(res)