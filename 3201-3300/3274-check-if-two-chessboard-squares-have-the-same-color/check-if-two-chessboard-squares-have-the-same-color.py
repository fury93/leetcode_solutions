class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        def getColor(pos):
            col = ord(pos[0]) - 96
            row = int(pos[1])
            return (row + col) & 1
        
        return getColor(c1) == getColor(c2)