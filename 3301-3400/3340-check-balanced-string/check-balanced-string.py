class Solution:
    def isBalanced(self, num: str) -> bool:
        sm = 0
        for i, n in enumerate(num):
            if i & 1:
                sm -= int(n)
            else:
                sm += int(n)
        
        return sm == 0
    