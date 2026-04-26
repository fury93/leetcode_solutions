class Solution:
    def minLength(self, s: str) -> int:
        stack, d = [], {'B': 'A', 'D': 'C'}
        for c in s:
            if stack and stack[-1] == d.get(c):
                stack.pop()
            else:
                stack.append(c)
    
        return len(stack)