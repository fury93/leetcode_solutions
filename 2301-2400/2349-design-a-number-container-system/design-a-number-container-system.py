from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.indexToNum = dict()
        self.numIndexes = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        if index in self.indexToNum:
            oldNum = self.indexToNum[index]
            self.numIndexes[oldNum].discard(index)
            if not self.numIndexes[oldNum]:
                del self.numIndexes[oldNum]
        self.indexToNum[index] = number
        self.numIndexes[number].add(index)

    def find(self, number: int) -> int:
        return self.numIndexes[number][0] if self.numIndexes[number] else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)