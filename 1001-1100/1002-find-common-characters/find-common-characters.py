from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = Counter(words[0])
        for word in words:
            d = d & Counter(word)

        return d.elements()