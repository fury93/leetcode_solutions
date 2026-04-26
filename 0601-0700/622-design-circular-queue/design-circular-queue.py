class Node:
    def __init__(self, val = -1):
        self.val = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, val) -> Node:
        newNode = Node(val)
        if self.size == 0:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return newNode

    def popLeft(self) -> bool:
        if self.size == 0: return False
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        del node
        self.size -= 1
        return True

    def peekLeft(self) -> int:
        if self.size == 0: return -1
        return self.head.val

    def peekRight(self) -> int:
        if self.size == 0: return -1
        return self.tail.val

    def getSize(self):
        return self.size

# LinkedList (it's one profit, does not pre-allocate memore fo unsunsed capacity)
# But it's not circular, where the idea to use already allocated memory
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.maxSize = k
        self.q = SLL()
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False 
        self.q.append(value)
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        return self.q.popLeft()

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.q.peekLeft()

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.q.peekRight()

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.q.getSize() == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.maxSize == self.q.getSize()

# Circular array
class MyCircularQueue2:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.data = [0] * k
        self.head = self.tail = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False 
        self.data[self.tail % len(self.data)] = value
        self.tail += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty(): return False 
        self.head += 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty(): return -1
        return self.data[self.head % len(self.data)]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty(): return -1
        return self.data[(self.tail-1) % len(self.data)]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == self.tail

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.tail - self.head == len(self.data)
        

class Node2:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class MyCircularQueue3:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        return True


    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        return self.head.value

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        # empty queue
        if self.count == 0:
            return -1
        return self.tail.value
    
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()