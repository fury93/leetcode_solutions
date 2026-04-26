class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard = dict(zip(keyboard, range(len(keyboard))))
        res, prevPos = 0, 0
        for ch in word:
            pos = keyboard[ch]
            res += abs(pos - prevPos)
            prevPos = pos
        return res
