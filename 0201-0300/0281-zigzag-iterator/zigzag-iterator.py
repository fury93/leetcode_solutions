class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.q = deque()
        for i, v in enumerate(self.vectors):
            if v: self.q.append((i, 0))

    def next(self) -> int:
        vector, pos = self.q.popleft()
        val = self.vectors[vector][pos]
        if pos+1 < len(self.vectors[vector]):
            self.q.append((vector, pos+1))
        return val

    def hasNext(self) -> bool:
        return len(self.q) > 0

# Two pointers
class ZigzagIterator2:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.p_elem = 0   # pointer to the index of element
        self.p_vec = 0    # pointer to the vector
        # variables for hasNext() function
        self.total_num = len(v1) + len(v2)
        self.output_count = 0

    def next(self) -> int:
        iter_num = 0
        ret = None

        # Iterate over the vectors
        while iter_num < len(self.vectors):
            curr_vec = self.vectors[self.p_vec]
            if self.p_elem < len(curr_vec):
                ret = curr_vec[self.p_elem]

            iter_num += 1
            self.p_vec = (self.p_vec + 1) % len(self.vectors)
            # increment the element pointer once iterating all vectors
            if self.p_vec == 0:
                self.p_elem += 1

            if ret is not None:
                self.output_count += 1
                return ret

        # no more element to output
        raise Exception


    def hasNext(self) -> bool:
        return self.output_count < self.total_num

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
