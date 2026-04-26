class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:

        # GET DIMENSIONS
        nrows, ncols = len(mat), len(mat[0])

        # SETUP THE PREFIX SUM MATRIX
        prefix = [[0 for _ in range(ncols + 1)] for _ in range(nrows + 1)]
        
        # FILL THE CELLS - TOP RECT + LEFT RECT - TOP LEFT DOUBLE-COUNTED RECT
        for i in range(nrows):
            for j in range(ncols):
                prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + mat[i][j]
        
        # for row in prefix:
        #     print(row)
            
        '''
        1. INITIALIZE MAX_SIDE = 0
        2. AT EACH CELL, WE'LL CHECK IF RECTANGLE (OR SQUARE) FROM [I - MAX, J - MAX] TO [I, J], BOTH INCLUSIVE, IS <= THRESHOLD
        '''
        
        # INITIALIZE MAX SIDE
        max_side = 0
        
        # CHECK IF RECTANGLE (OR SQUARE) FROM [I - MAX, J - MAX] TO [I, J] <= THRESHOLD
        for i in range(nrows):
            for j in range(ncols): 
                
                # CHECK IF WE CAN SUBTRACT MAX_SIDE
                if min(i, j) >= max_side:
                    curr = prefix[i + 1][j + 1]
                    top = prefix[i - max_side][j + 1]
                    left = prefix[i + 1][j - max_side]
                    topLeft = prefix[i - max_side][j - max_side]
                    total = curr - top - left + topLeft
                    
                    # print(f"CURR : {curr} | TOP : {top} | LEFT : {left} | TOP_LEFT : {topLeft}")
                    # print(f"TOTAL : {total}\n")
                    
                    # UPDATE MAX_SIDE IFF TOTAL <= THRESHOLD
                    if total <= threshold:
                        max_side += 1
                
        # RETURN MAX SIDE
        return max_side