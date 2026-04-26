from sortedcontainers import SortedList
from heapq import heappop, heappush, heapreplace

class SORTracker2:

    def __init__(self):
        self.data = SortedList()
        self.idx = -1

    def add(self, name: str, score: int) -> None:
        self.data.add((-score, name))

    def get(self) -> str:
        self.idx += 1
        return self.data[self.idx][1]

class MinHeapLocation:
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __lt__(self, other):
        return self.val < other.val or (self.val == other.val and self.name > other.name)


class MaxHeapLocation:
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __lt__(self, other):
        return self.val > other.val or (self.val == other.val and self.name < other.name)

class SORTracker:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.idx = 1

    def add(self, name: str, score: int) -> None:
        
        minLoc = MinHeapLocation(name, score)
        if len(self.minHeap) < self.idx:
            heappush(self.minHeap, minLoc)
        elif minLoc > self.minHeap[0]:
            loc = heapreplace(self.minHeap, minLoc)
            heappush(self.maxHeap, MaxHeapLocation(loc.name, loc.val))
        else:
            heappush(self.maxHeap, MaxHeapLocation(name, score))
        return
        minLoc = MinHeapLocation(name, score)
        self.minHeap.append(minLoc)
        if len(self.minHeap) > self.idx:
            loc = heappop(self.minHeap)
            heappush(self.maxHeap, MaxHeapLocation(loc.name, loc.val))
        return
        
        #self.debug()

    def get(self) -> str:
        curLocationName = self.minHeap[0].name
        self.idx += 1
        if self.maxHeap:
            loc = heappop(self.maxHeap)
            heappush(self.minHeap, MinHeapLocation(loc.name, loc.val))
        #self.debug()
        return curLocationName

    def debug(self):
        print('min =', self.minHeap, 'max=', self.maxHeap, self.idx)


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()