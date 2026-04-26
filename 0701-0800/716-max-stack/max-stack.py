from sortedcontainers import SortedList
class MaxStack:

    def __init__(self):
        self.stack = SortedList()
        self.max_stack = SortedList()
        self.idx = 0

    def push(self, x: int) -> None:
        self.stack.add((self.idx, x))
        self.max_stack.add((x, self.idx))
        self.idx += 1

    def pop(self) -> int:
        idx, x = self.stack.pop()
        self.max_stack.remove((x, idx))
        return x

    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.max_stack[-1][0]
        
    def popMax(self) -> int:
        x, idx = self.max_stack.pop()
        self.stack.remove((idx, x))
        return x
        
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()