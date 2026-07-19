class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack, visited, last_pos = [], set(), dict()
        for i, c in enumerate(s):
            last_pos[c] = i
     
        for i, c in enumerate(s):
            if c in visited: continue 
            while stack and stack[-1] > c and last_pos[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)

        return ''.join(stack)