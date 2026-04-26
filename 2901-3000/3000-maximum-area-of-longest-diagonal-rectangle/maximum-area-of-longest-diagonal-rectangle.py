class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return max((h*h+w*w, h*w) for h,w in dimensions)[1]