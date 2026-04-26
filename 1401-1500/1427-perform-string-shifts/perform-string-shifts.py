class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        pos = 0
        for direction, amount in shift:
            if direction == 0: pos += amount
            else: pos -= amount
        pos = pos % len(s)
        
        return s[pos:] + s[:pos]
