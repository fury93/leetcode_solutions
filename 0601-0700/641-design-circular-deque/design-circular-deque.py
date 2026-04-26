class Node:
    def __init__(self, val = None):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.limit = k
        self.size = 0
        self.start = Node()
        self.end = Node()
        self.start.next = self.end
        self.end.prev = self.start

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        node = Node(value)
        left, right = self.start, self.start.next
        node.prev, node.next = left, right
        left.next, right.prev = node, node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        node = Node(value)
        left, right = self.end.prev, self.end
        node.prev, node.next = left, right
        left.next, right.prev = node, node
        self.size += 1
        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        firstNode = self.start.next
        left, right = firstNode.prev, firstNode.next
        left.next, right.prev = right, left
        del firstNode
        self.size -= 1
        return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        lastNode = self.end.prev
        left, right = lastNode.prev, lastNode.next
        left.next, right.prev = right, left
        del lastNode
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.start.next.val

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.end.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()