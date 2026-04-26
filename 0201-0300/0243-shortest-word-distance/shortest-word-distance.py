class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        L = len(wordsDict)
        res, preWord1, preWord2 = L, -L, -L 
        for i, w in enumerate(wordsDict):
            if w == word1:
                res = min(res, i - preWord2)
                preWord1 = i
            elif w == word2:
                res = min(res, i - preWord1)
                preWord2 = i
        
        return res
