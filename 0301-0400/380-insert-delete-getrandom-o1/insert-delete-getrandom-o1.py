class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.indices: return False
        self.indices[val] = len(self.arr)
        self.arr.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.indices: return False
        
        removeIdx, lastVal = self.indices[val], self.arr[-1]
        self.arr[removeIdx] = lastVal
        self.indices[lastVal] = removeIdx
    
        self.indices.pop(val)
        self.arr.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)