class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similar = defaultdict(set)
        for word1, word2 in similarPairs:
            similar[word1].add(word2)
            similar[word2].add(word1)
        
        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2 and w1 not in similar[w2] and w2 not in similar[w1]:
                return False

        return True