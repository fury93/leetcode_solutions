class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a_cnt = s.count('a')
        return abs(a_cnt - (len(s) - a_cnt))