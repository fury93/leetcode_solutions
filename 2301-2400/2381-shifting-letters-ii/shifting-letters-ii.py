class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            change = 1 if direction == 1 else -1
            diff[start] += change
            diff[end+1] -= change
        
        diff = list(accumulate(diff))
        
        return ''.join(chr((ord(ch) - 97 + diff[i]) % 26 + 97) for i, ch in enumerate(s))