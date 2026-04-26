class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxArea = [], 0
        for i, n in enumerate(chain(heights, [0])):
            while stack and heights[stack[-1]] > n:
                h = heights[stack.pop()]
                w = i if not stack else i - 1 - stack[-1]
                maxArea = max(maxArea, h * w)
            stack.append(i)

        return maxArea

        