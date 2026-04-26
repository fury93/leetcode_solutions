class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = deque()
        self.uniqNums = dict()
        for num in nums:
            self.add(num)
        

    def showFirstUnique(self) -> int:
        while self.nums and not self.uniqNums[self.nums[0]]:
            self.nums.popleft()

        return self.nums[0] if self.nums else -1

    def add(self, value: int) -> None:
        if value in self.uniqNums:
            self.uniqNums[value] = False
        else:
            self.uniqNums[value] = True
            self.nums.append(value)

class FirstUnique3:

    def __init__(self, nums: List[int]):
        self._queue = OrderedDict()
        self._is_unique = {}
        for num in nums:
            # Notice that we're calling the "add" method of FirstUnique; not of the queue. 
            self.add(num)
        
    def showFirstUnique(self) -> int:
        # Check if there is still a value left in the queue. There might be no uniques.
        if self._queue:
            # We don't want to actually *remove* the value.
            # Seeing as OrderedDict has no "get first" method, the way that we can get
            # the first value is to create an iterator, and then get the "next" value
            # from that. Note that this is O(1).
            return next(iter(self._queue))
        return -1
        
    def add(self, value: int) -> None:
        # Case 1: We need to add the number to the queue and mark it as unique. 
        if value not in self._is_unique:
            self._is_unique[value] = True
            self._queue[value] = None
        # Case 2: We need to mark the value as no longer unique and then 
        # remove it from the queue.
        elif self._is_unique[value]:
            self._is_unique[value] = False
            self._queue.pop(value)
        # Case 3: We don't need to do anything; the number was removed from the queue
        # the second time it occurred.

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)