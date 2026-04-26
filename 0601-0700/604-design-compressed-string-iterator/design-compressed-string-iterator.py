class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.nextLetterPos = 0
        self.letter = None
        self.letterCnt = 0
        
    def __moveNext(self):
        if self.nextLetterPos >= len(self.s):
            raise StopIteration
        self.letter = self.s[self.nextLetterPos]
        # calculate number of new letter
        startPos = curPos = self.nextLetterPos + 1
        while curPos < len(self.s) and self.s[curPos].isdigit():
            curPos += 1
        self.letterCnt = int(self.s[startPos:curPos])
        self.nextLetterPos = curPos

    def next(self) -> str:
        if not self.hasNext(): return ' '
        if self.letterCnt == 0:
            self.__moveNext()
        self.letterCnt -= 1
        return self.letter

    def hasNext(self) -> bool:
        return self.nextLetterPos < len(self.s) or self.letterCnt > 0