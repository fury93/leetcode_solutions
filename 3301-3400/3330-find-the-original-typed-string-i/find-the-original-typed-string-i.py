class Solution:
    def possibleStringCount(self, word: str) -> int:
        return 1 + sum(len(list(group)) - 1 for _, group in groupby(word))