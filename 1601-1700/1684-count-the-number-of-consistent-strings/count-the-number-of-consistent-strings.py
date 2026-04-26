class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(set(allowed) >= set(w) for w in words)

    def countConsistentStrings2(self, allowed: str, words: List[str]) -> int:
        res = 0
        allowed = set(allowed)
        for word in words:
            if set(word) <= allowed:
                res +=1

        return res