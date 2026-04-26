class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {k:i for i, k in enumerate(order)}

        for i in range(1, len(words)):
            for prev, cur in zip(words[i-1], words[i]):
                if d[prev] < d[cur]: break
                elif d[prev] > d[cur]: return False
            else:
                if len(words[i-1]) > len( words[i]): return False
        
        return True

        
        