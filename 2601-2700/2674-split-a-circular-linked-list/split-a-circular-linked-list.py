class Solution:
    def splitCircularLinkedList(self, start1: Optional[ListNode]) -> List[Optional[ListNode]]:
        cur, cnt = start1, 1
        # find the lenght and the last node
        while cur.next != start1:
            cur, cnt = cur.next, cnt + 1
        end = cur # save the last node
          
        mid = math.ceil(cnt / 2)
        # after interation cur will be the last node for block1
        while mid > 0:
            cur, mid = cur.next, mid - 1

        # 1(start1) -> 2(cur) -> 3(cur.next) -> 4(end)
        start2 = cur.next
        end.next = start2
        cur.next = start1

        return [start1, start2]
        


