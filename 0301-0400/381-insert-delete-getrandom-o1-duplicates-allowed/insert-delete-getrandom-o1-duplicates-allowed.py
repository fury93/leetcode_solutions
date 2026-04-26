class RandomizedCollection:

    def __init__(self):
        self.d = defaultdict(set)
        self.arr = []

    def insert(self, val: int) -> bool:
        isNew = len(self.d[val]) == 0
        self.d[val].add(len(self.arr))
        self.arr.append(val) 
        
        return isNew
        

    def remove(self, val: int) -> bool:
        if not self.d[val]: return False

        removeId, lastVal = self.d[val].pop(), self.arr[-1]
        self.arr[removeId] = lastVal
        self.d[lastVal].add(removeId)
        self.d[lastVal].discard(len(self.arr)-1)
        self.arr.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()