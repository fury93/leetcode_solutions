class LinkedList:
    def __init__(self, key, next = None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.data = [LinkedList(0) for _ in range(10000)]
        
    def key(self, key):
        return key % 9999

    def add(self, key: int) -> None:
        cur = self.data[self.key(key)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = LinkedList(key)
        
    def remove(self, key: int) -> None:
        cur = self.data[self.key(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.data[self.key(key)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)