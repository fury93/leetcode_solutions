class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if k == len(num): return '0'

        for i, n in enumerate(num):
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -=1
            stack.append(n)
        
        if k > 0:
            stack = stack[:-k]
        
        return ''.join(stack).lstrip('0') or '0'