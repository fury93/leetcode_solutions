class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.dummy_start = Node()
        self.dummy_end = Node()
        self.dummy_start.next = self.dummy_end
        self.dummy_end.prev = self.dummy_start

    def appendleft(self, node) -> Node:
        left, right = self.dummy_start, self.dummy_start.next
        node.next = right
        right.prev = node
        left.next = node
        node.prev = left
        
        return node

    def remove(self, node) -> Node:
        left, right = node.prev, node.next
        left.next = right
        right.prev = left
        
        return node

    def move_to_start(self, node):
        return self.appendleft(self.remove(node))

    def pop(self):
        return self.remove(self.dummy_end.prev)
    
    def peek(self):
        return self.dummy_end.prev.val

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.dll = DLL()

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        
        node = self.cache[key]
        self.dll.move_to_start(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.dll.remove(self.cache[key])
            node.val = value
        else:
            node = Node(key, value)
            self.cache[key] = node
        
        self.dll.appendleft(node)
        
        if len(self.cache) > self.capacity:
            self.cache.pop(self.dll.pop().key)


class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.__evict(key)
        self.__addToEnd(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.__delete(key)

        node = Node(key, value)
        self.cache[key] = node
        self.dll.appendleft(node)
        
        if len(self.cache) > self.capacity:
            self.__delete(self.head.next.key)
    
    def __evict(self, key) -> Node: 
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        return node

    def __delete(self, key) -> None:
        deleteNode = self.__evict(key)
        del deleteNode
        del self.cache[key]

    def __addToEnd(self, node) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

class LRUCache3:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache[key] = self.cache.pop(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.pop(next(iter(self.cache)))

class LRUCache1:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(False)