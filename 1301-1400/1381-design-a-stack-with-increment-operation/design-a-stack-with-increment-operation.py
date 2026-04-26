class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
        self.bonus = []
        
    def push(self, x: int) -> None:
        if self.__l() == self.size: return
        self.stack.append(x)
        self.bonus.append(0)
        
    def pop(self) -> int:
        if not self.__l(): return -1
        if self.__l() > 1:
            self.bonus[-2] += self.bonus[-1]
        return self.stack.pop() + self.bonus.pop()

    def increment(self, k: int, val: int) -> None:
        if not self.__l(): return

        k = min(len(self.stack), k) - 1
        self.bonus[k] += val
        
    def __l(self) -> int:
        return len(self.stack)

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)