# similar problem https://leetcode.com/problems/broken-calculator/description/
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1 and maxDoubles > 0:
            moves += 1 + (target & 1)
            maxDoubles -= 1
            target >>= 1

        return moves + target - 1
            