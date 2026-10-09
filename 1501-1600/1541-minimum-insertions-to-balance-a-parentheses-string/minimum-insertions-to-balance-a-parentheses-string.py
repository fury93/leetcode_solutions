class Solution:
    # if meet ( => needClosed += 2 also check previous number of closed brackets
    # if closed brackets is odd => add 1 missing closet bracket to result
    # if meet ) => needClosed -= 1
    # if needClosed < 0 => add 1 missing opened bracke to result
    # return res + needClosed

    def minInsertions(self, s: str) -> int:
        res, needClosed = 0, 0
        for ch in s:
            if ch == '(':
                if needClosed & 1:
                    res += 1
                    needClosed -= 1
                needClosed += 2
            else:
                needClosed -= 1
                if needClosed < 0:
                    res += 1
                    needClosed = 1

        return res + needClosed
                    

        