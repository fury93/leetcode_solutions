#from sortedcontainers import SortedList
class TwoSum:

    def __init__(self):
        self.data = defaultdict(int)
        #self.data = SortedList()
        #self.data = []

    def add(self, number: int) -> None:
        self.data[number] += 1
        #self.data.add(number)
        #self.data.append(number)

    def find(self, value: int) -> bool:
        for n1 in self.data:
            n2 = value - n1
            if n2 in self.data:
                if n2 != n1 or self.data[n2] > 1: return True
        
        return False
        
        #solution3
        #self.data.sort()
        # solution2
        l, r = 0, len(self.data) - 1
        while l < r:
            curVal = self.data[l] + self.data[r]
            if curVal < value:
                l += 1
            elif curVal > value:
                r -= 1
            else:
                return True
        return False