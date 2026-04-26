class Solution:
    def minMoves(self, rooks):
        min_moves = 0

        # Store the count of rooks in each row and column.
        row = [0] * len(rooks)
        col = [0] * len(rooks)
        for r in rooks:
            row[r[0]] += 1
            col[r[1]] += 1

        row_min_moves = 0
        col_min_moves = 0
        for i in range(len(rooks)):
            # Difference between the rooks count at row and column and one.
            row_min_moves += row[i] - 1
            col_min_moves += col[i] - 1

            # Moves required for row and column constraints.
            min_moves += abs(row_min_moves) + abs(col_min_moves)

        return min_moves

class Solution2:
    def minMoves(self, rooks: List[List[int]]) -> int:
        n = len(rooks)
        
        # Sort rooks by their row positions
        rooks.sort(key=lambda x: x[0])
        
        # Target positions after sorting by rows
        targetRows = list(range(n))
        
        # Calculate moves needed to place each rook in its target row
        rowMoves = sum(abs(rooks[i][0] - targetRows[i]) for i in range(n))
        
        # Sort rooks by their column positions
        rooks.sort(key=lambda x: x[1])
        
        # Target positions after sorting by columns
        targetCols = list(range(n))
        
        # Calculate moves needed to place each rook in its target column
        colMoves = sum(abs(rooks[i][1] - targetCols[i]) for i in range(n))
        
        # Total moves is the sum of row moves and column moves
        return rowMoves + colMoves        