class Solution:
    def largestSquareArea2(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        res = 0 # the rectange side
        coordinats = sorted(zip(bottomLeft, topRight))
        
        for i in range(len(coordinats)):
            for j in range(i + 1, len(coordinats)):
                ax1, ay1 = coordinats[i][0] #a[0]
                ax2, ay2 = coordinats[i][1] #a[1]
                bx1, by1 = coordinats[j][0] #b[0]
                bx2, by2 = coordinats[j][1] #b[1]

                overlapX = min(ax2, bx2) - max(ax1, bx1)
                overlapY = min(ay2, by2) - max(ay1, by1)

                # move to the next i-th rectangle, no more intersactions between i-th and j-th rectangles
                if overlapX < 0 and overlapY < 0: break 
                if overlapX > 0 and overlapY > 0:
                    minSquareSide = min(overlapX, overlapY)
                    res = max(res, minSquareSide)

        return res * res

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        res = 0 # the rectange side
        coordinats = list(zip(bottomLeft, topRight))
        
        for ((ax1, ay1), (ax2, ay2)), ((bx1, by1), (bx2, by2)) in combinations(coordinats, 2):
            overlapX = min(ax2, bx2) - max(ax1, bx1)
            overlapY = min(ay2, by2) - max(ay1, by1)

            if overlapX > 0 and overlapY > 0:
                minSquareSide = min(overlapX, overlapY)
                res = max(res, minSquareSide)

        return res * res