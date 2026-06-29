class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(x in word for x in patterns)