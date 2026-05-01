class Solution:
    def canAliceWin(self, n: int) -> bool:
        isAliceTurn, remove = True, 10
        
        while n >= remove:
            n -= remove
            remove -= 1
            isAliceTurn = not isAliceTurn

        return not isAliceTurn