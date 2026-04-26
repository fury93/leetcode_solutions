class FreqStack:

    def __init__(self):
        self.stack = [[]]
        self.freq = defaultdict(int)
        self.maxFreq = 0
        

    def push(self, val: int) -> None:
        self.freq[val] += 1
        curFreq = self.freq[val]
        if curFreq > self.maxFreq:
            self.maxFreq = curFreq
            self.stack.append([val])
        else:
            self.stack[curFreq].append(val)

    def pop(self) -> int:
        val = self.stack[self.maxFreq].pop()
        self.freq[val] -= 1
        if len(self.stack[self.maxFreq]) == 0:
            self.stack.pop()
            self.maxFreq -=1
        return val
        
class FreqStack2:

    def __init__(self):
        self.stack = defaultdict(list)
        self.freq = defaultdict(int)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        curFreq = self.freq[val]
        self.stack[curFreq].append(val)
        self.maxFreq = max(self.maxFreq, curFreq)

    def pop(self) -> int:
        val = self.stack[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.stack[self.maxFreq]:
            # del self.stack[self.maxFreq]
            self.maxFreq -=1
        
        return val
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()