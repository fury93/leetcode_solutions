# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.cur = self.it.next() if self.it.hasNext() else None
        

    def peek(self):
        return self.cur

    def next(self):
        res = self.cur
        self.cur = self.it.next() if self.it.hasNext() else None
        return res

    def hasNext(self):
        return bool(self.cur)

class PeekingIterator2:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.cur = None
        self.it = iterator
        

    def peek(self):
        if not self.cur and self.it.hasNext():
            self.cur = self.next()
        return self.cur

    def next(self):
        if self.cur:
            res = self.cur
            self.cur = None
        else:
            res = self.it.next()
        return res

    def hasNext(self):
        return bool(self.cur or self.it.hasNext())

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].