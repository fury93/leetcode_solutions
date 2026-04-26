class Solution:
    def maxDifference(self, s: str) -> int:
        maxOdd, minEven = -math.inf, math.inf

        for freq in Counter(s).values():
            if freq & 1:
                maxOdd = max(maxOdd, freq)
            else:
                minEven = min(minEven, freq)
        
        return maxOdd - minEven
            


