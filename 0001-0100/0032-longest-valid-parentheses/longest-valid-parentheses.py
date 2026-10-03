class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, maxLen = [-1], 0
        for i, br in enumerate(s):
            if br == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                  stack.append(i)
                else:    
                  maxLen = max(maxLen, i - stack[-1])
        return maxLen