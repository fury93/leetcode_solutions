class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1_1,y1_1,x2_1,y2_1 = rec1
        x1_2,y1_2,x2_2,y2_2 = rec2
        width = min(x2_1,x2_2) - max(x1_1, x1_2)
        height = min(y2_1, y2_2) - max(y1_1, y1_2)
        return width > 0 and height > 0