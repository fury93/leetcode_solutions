"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
from functools import reduce
from operator import concat
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        schedule = sorted(reduce(concat, schedule, []), key = lambda s: s.start)
        freeTime, freeStart = [], schedule[0].end

        for i in range(1, len(schedule)):
            time = schedule[i]
            if time.start > freeStart:
                freeTime.append(Interval(freeStart, time.start))
            freeStart = max(freeStart, time.end)
        return freeTime