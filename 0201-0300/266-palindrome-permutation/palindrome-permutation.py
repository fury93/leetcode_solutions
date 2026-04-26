class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(v % 2 for v in Counter(s).values()) < 2
    
    def canPermutePalindrome2(self, s: str) -> bool:
        isAllowOdd = len(s) & 1

        for v in Counter(s).values():
            if v & 1:
                if not isAllowOdd: return False
                isAllowOdd = False
            
        return True