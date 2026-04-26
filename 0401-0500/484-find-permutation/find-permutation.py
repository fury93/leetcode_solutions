class Solution:
    # stack, look editorial 1st solution
    def findPermutation(self, s: str) -> List[int]:
        res = [None] * (len(s) + 1)
        stack, j = [], 0

        for i, ch in enumerate(chain(s, 'I'), start = 1):
            stack.append(i)
            if ch == 'I':
                while stack:
                    res[j] = stack.pop()
                    j += 1
        
        return res
            
    # todo in progress
    def findPermutation2(self, s: str) -> List[int]:
        res, maxN, decrCnt = [None] * (len(s) + 1), 1, 0

        for ch in s:
            if ch == 'I':
                maxN += 1
                res.append(maxN)
                decrCnt = 0
            else:
                decrCnt += 1

