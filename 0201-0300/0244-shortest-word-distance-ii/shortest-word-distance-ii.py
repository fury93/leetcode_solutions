class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.words[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        w1p, w2p = self.words[word1], self.words[word2]
        res, l1, l2 = math.inf, 0, 0 

        while l1 < len(w1p) and l2 < len(w2p):
            p1, p2 = w1p[l1], w2p[l2]
            res = min(res, abs(p1 -p2))
            if p1 > p2:
                l2 += 1
            else:
                l1 += 1
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)