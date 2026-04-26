class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])
        elif self.min_stack[-1][0] == val:
            self.min_stack[-1][1] += 1
        
    def pop(self) -> None:
        val = self.stack.pop()
        if self.min_stack[-1][0] == val:
            self.min_stack[-1][1] -= 1
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]

class MinStack2:

    def __init__(self):
        self.data = []
        
    def push(self, val: int) -> None:
        curMin = min(val, self.data[-1][1]) if self.data else val
        self.data.append((val, curMin))
        
    def pop(self) -> None:
        self.data.pop() if self.data else None

    def top(self) -> int:
        return self.data[-1][0] if self.data else None

    def getMin(self) -> int:
        if not self.data:
            return float('-inf')
        return self.data[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()