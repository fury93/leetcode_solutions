# Using iterator
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        def generator(vec):
            for row in vec:
                for val in row:
                    yield val
        
        self.gen = generator(vec)
        self.cur = next(self.gen, None)

    def next(self) -> int:
        res = self.cur
        self.cur = next(self.gen, None)
        return res
        
    def hasNext(self) -> bool:
        return self.cur is not None

class Vector2D_2:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.outer = 0
        self.inner = 0

    def __moveToNext(self):
        while self.outer < len(self.vec) and len(self.vec[self.outer]) == self.inner:
            self.outer += 1
            self.inner = 0

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration
        val = self.vec[self.outer][self.inner]
        self.inner += 1
        return val
        
    def hasNext(self) -> bool:
        self.__moveToNext()
        return self.outer < len(self.vec)