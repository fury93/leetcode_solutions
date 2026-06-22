class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textMap = Counter(text)
        balloonMap = Counter("balloon")
        
        res = len(text)
        for c in balloonMap:
            res = min(res, textMap[c] // balloonMap[c])
        
        return res