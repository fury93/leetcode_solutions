# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    # BFS
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        res, q, depth = 0, deque(nestedList), 1
        while q:
            for _ in range(len(q)):
                item = q.popleft()
                if item.isInteger():
                    res += item.getInteger() * depth
                else:
                    q.extend(item.getList())
            depth += 1

        return res

    # DFS
    def depthSum2(self, nestedList: List[NestedInteger]) -> int:
        self.res = 0
        def calculator(items, depth):
            for item in items:
                if item.isInteger():
                    self.res += item.getInteger() * depth
                else:
                    calculator(item.getList(), depth + 1)

        calculator(nestedList, 1)

        return self.res
        