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
    def depthSumInverse(self, nestedList):
        depth, res, d = 1, 0, {}
        while nestedList:
            d[depth] = [x.getInteger() for x in nestedList if x.isInteger()]
            nestedList = sum([x.getList() for x in nestedList if not x.isInteger()], [])
            depth += 1
        for level_depth, values in d.items():
            res += (depth-level_depth) * sum(values)
        return res
        
class Solution3(object):
    def helper(self, nestedList, level, cache):
        self.max_level = max(self.max_level, level)
        for x in nestedList:
            if x.isInteger():
                cache[level] += x.getInteger()
            else:
                self.helper(x.getList(), level+1, cache)
        return
    
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        cache, self.max_level = defaultdict(int), -1
        self.helper(nestedList, 1, cache)
        total_sum = 0
        for k,v in cache.items():
            total_sum = total_sum + v*(self.max_level-k+1)
        return total_sum

class Solution2(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        total_sum, level_sum = 0, 0
        while len(nestedList):
            next_level_list = []
            for x in nestedList:
                if x.isInteger():
                    level_sum += x.getInteger()
                else:
                    for y in x.getList():
                        next_level_list.append(y)
            total_sum += level_sum
            nestedList = next_level_list
        return total_sum