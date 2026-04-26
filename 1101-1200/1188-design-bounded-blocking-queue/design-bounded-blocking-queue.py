import threading

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.queue = deque([])
        self.enqueueLock = threading.Semaphore(capacity)
        self.dequeueLock = threading.Semaphore(0)

    def enqueue(self, element: int) -> None:
        self.enqueueLock.acquire()
        self.queue.append(element)
        self.dequeueLock.release()

    def dequeue(self) -> int:
        self.dequeueLock.acquire()
        element = self.queue.popleft()
        self.enqueueLock.release()
        return element

    def size(self) -> int:
        return len(self.queue)

class BoundedBlockingQueue2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.editing = threading.Lock()
      
        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
      self.pushing.acquire()
      self.editing.acquire()
      
      self.queue.append(element)
      
      self.editing.release()
      self.pulling.release()

    def dequeue(self) -> int:
        self.pulling.acquire()
        self.editing.acquire()
        
        res = self.queue.popleft()
        
        self.editing.release()
        self.pushing.release()
        return res

    def size(self) -> int:
      return len(self.queue)