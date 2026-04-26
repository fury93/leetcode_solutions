class Solution:
    # O(Q + 64)
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res, queen_set = [], set(map(tuple, queens))
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (-1, -1), (-1, 1), (1, -1),  # diagonals
        ]
        
        for dr, dc in directions:
            r, c = king
            while 0 <= (r:= r + dr) < 8 and 0 <= (c:= c + dc) < 8:
                if (r, c) in queen_set:
                    res.append([r, c])
                    break
                
        return res
