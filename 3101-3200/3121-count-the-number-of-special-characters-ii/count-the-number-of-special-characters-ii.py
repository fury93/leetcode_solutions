class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower, upper, ignore = 0, 0, 0
        for ch in word:
            bit = 1 << ord(ch.lower()) - 97
            
            if ch.islower():
                lower |= bit
                if upper & bit:
                    ignore |= bit
            else:
                upper |= bit
        
        return (lower & upper & ~ignore).bit_count()
            