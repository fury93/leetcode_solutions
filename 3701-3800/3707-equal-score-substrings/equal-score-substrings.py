class Solution:
    def scoreBalance(self, s: str) -> bool:
        scores = list(accumulate(s, lambda x, y: x + ord(y) - 96, initial = 0))
        return not scores[-1] & 1 and scores[-1]//2 in scores
    
    def scoreBalance2(self, s: str) -> bool:
        weights = [ord(ch) - 96 for ch in s]
        scores = list(accumulate(weights))
        return not scores[-1] & 1 and scores[-1]//2 in scores