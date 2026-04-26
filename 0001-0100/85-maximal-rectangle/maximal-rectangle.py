class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea, heights = 0, [0] * (len(matrix[0]) + 1)
        
        for row in matrix:
            for i, v in enumerate(row):
                heights[i] = heights[i] + 1 if v == '1' else 0
            stack = [-1]
            for i, v in enumerate(heights):
                while stack and heights[stack[-1]] > v:
                    h = heights[stack.pop()]
                    w = i - 1 - stack[-1]
                    maxArea = max(maxArea, h*w)
                stack.append(i)
        
        return maxArea