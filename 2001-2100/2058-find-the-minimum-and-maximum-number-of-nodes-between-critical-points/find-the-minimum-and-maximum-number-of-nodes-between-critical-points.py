class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, cur  = head, head.next
        pos, firstPos, prevPos, minDist = 0, None, None, math.inf
        
        while cur.next:
            pos += 1
            if prev.val < cur.val > cur.next.val or prev.val > cur.val < cur.next.val:
                if prevPos:
                    minDist = min(minDist, pos - prevPos)
                    prevPos = pos
                else:
                    firstPos = prevPos = pos
                
            cur, prev = cur.next, cur

        if minDist == math.inf:
            return [-1, -1]

        return [minDist, prevPos - firstPos]
    
    def nodesBetweenCriticalPoints2(self, head: Optional[ListNode]) -> List[int]:
        prev, cur, idx, i = head, head.next, [], 1
        while cur and cur.next:
            if prev.val < cur.val > cur.next.val or prev.val > cur.val < cur.next.val:
                idx.append(i)
            prev = cur
            cur = cur.next
            i += 1

        if len(idx) < 2:
            return [-1, -1]
        
        minDist = min(j - i for i, j in pairwise(idx))
        maxDist = idx[-1] - idx[0]

        return [minDist, maxDist]
