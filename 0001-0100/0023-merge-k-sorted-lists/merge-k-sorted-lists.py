# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # filter out empty lists
        lists = list(filter(lambda x: x, lists))
        # create a heap with elements in form (val, idx), where
        # val - value of the current head
        # idx - index of the list in a filtered list
        heap = list(zip(map(lambda x: x.val, lists), range(len(lists))))
        heapify(heap)
        # pick the list with minimum value in the head
        # attach the head to the resulting list
        # move the head and add it to the heap
        root = ListNode()
        head = root
        while heap:
            _, i = heappop(heap)
            head.next, head, lists[i] = lists[i], lists[i], lists[i].next
            if lists[i]: heappush(heap, (lists[i].val, i))
        return root.next
        