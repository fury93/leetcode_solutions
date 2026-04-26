class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.backbone = Node()
        self.length = 0

    def get(self, index: int) -> int:
        if index > self.length-1: return -1
        
        node = self.backbone.next
        for _ in range(index):
            node = node.next
        
        return node.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val, self.backbone.next)
        self.backbone.next = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        lastNode = self.backbone
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length: return
        
        if index == self.length:
            self.addAtTail(val)
            return

        prevNode = self.backbone
        for _ in range(index):
            prevNode = prevNode.next

        node = Node(val, prevNode.next)
        prevNode.next = node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length-1: return
        
        prevNode = self.backbone
        for _ in range(index):
            prevNode = prevNode.next
        
        prevNode.next = prevNode.next.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)