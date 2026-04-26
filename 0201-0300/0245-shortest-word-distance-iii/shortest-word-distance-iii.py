class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        L, isOneWord = len(wordsDict), word1 == word2
        res, p1, p2 = L, -L, -L

        for i, w in enumerate(wordsDict):
            if w == word1:
                if isOneWord: p2 = p1 # p1 is always > p2 for one word
                p1 = i
            elif w == word2:
                p2 = i
            else:
                continue
            
            res = min(res, abs(p1 - p2))
        return res


