class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        needOpen, needClose = 0, 0
        for c in s:
            if c == '(':
                needClose +=1
            else:
                if needClose > 0:
                    needClose -=1
                else:
                    needOpen +=1
        return needOpen + needClose

    def minAddToMakeValid2(self, s: str) -> int:
        stack = []
        for c in s:
            if stack and stack[-1] == '(' and c == ')':
                stack.pop()
            else:
                stack.append(c)

        return len(stack)