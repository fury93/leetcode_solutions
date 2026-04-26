class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return ord(coordinates[0]) % 2 != int(coordinates[1]) % 2

    def squareIsWhite2(self, coordinates: str) -> bool:
        col = ord(coordinates[0]) - ord('a') + 1
        row = int(coordinates[1])

        return row % 2 != col % 2