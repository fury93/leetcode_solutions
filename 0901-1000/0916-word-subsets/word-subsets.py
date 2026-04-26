class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        bFreq = Counter()
        for w2 in words2:
            bFreq |= Counter(w2)
        
        return [w1 for w1 in words1 if bFreq <= Counter(w1)]