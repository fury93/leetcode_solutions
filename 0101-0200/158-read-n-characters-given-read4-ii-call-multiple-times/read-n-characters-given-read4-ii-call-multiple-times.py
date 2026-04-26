class Solution:
    def __init__(self):
        self.buf4 = [''] * 4
        self.i4 = 0
        self.n4 = 0
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n:
            if self.i4 == self.n4:
                self.i4 = 0
                self.n4 = read4(self.buf4)
                if self.n4 == 0:
                    break
            buf[i] = self.buf4[self.i4]
            self.i4 += 1
            i += 1
        return i

class Solution2:
    def __init__(self):
        self.buf4 = [''] * 4
        self.buf_index = 0
        self.buf_size = 0


    def read(self, buf: List[str], n: int) -> int:
        index = 0
        while index < n:
            if self.buf_index == self.buf_size: # read new buf4
                self.buf_size = read4(self.buf4)
                self.buf_index = 0
                if self.buf_size == 0: # end of file
                    break
            
            while index < n and self.buf_index < self.buf_size:
                buf[index] = self.buf4[self.buf_index]
                self.buf_index += 1
                index += 1
            
        return index