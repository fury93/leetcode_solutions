class Solution:
    def isValid(self, s: str) -> bool:
        #odd string
        if len(s) % 2 == 1:
            return False
        
        brackets = {'{': '}', '(': ')', '[': ']'}
        stack = []
        
        for char in s:
            if char in brackets:
                stack.append(char)
            elif not stack or brackets[stack.pop()] != char:
                return False
        
        return not stack