# One queue: push - O(N), pop - O(1)
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        q = self.q
        q.append(x)
        for _ in range(len(q)-1):
            q.append(q.popleft())
        
    def pop(self) -> int:
        return self.q.popleft()
        
    def top(self) -> int:
        return self.q[0]
        
    def empty(self) -> bool:
        return not len(self.q)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()