class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        index, time = events[0][0], events[0][1]
        for i in range(1, len(events)):
            curTimeDiff = events[i][1] - events[i-1][1]
            curIndex = events[i][0]
            if curTimeDiff > time:
                index, time = curIndex, curTimeDiff
            elif curTimeDiff == time and curIndex < index:
                index = curIndex

        return index