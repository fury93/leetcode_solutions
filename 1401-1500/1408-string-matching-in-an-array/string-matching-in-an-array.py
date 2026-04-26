class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        allWords = ' '.join(words)
        return [w for w in words if allWords.count(w) > 1]