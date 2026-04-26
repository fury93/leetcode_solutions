class Solution:
    def kEmptySlots(self, flowers, k):
        active = []
        for day, flower in enumerate(flowers, 1):
            i = bisect.bisect(active, flower)
            for neighbor in active[i-(i>0):i+1]:
                if abs(neighbor - flower) - 1 == k:
                    return day
            active.insert(i, flower)
        return -1

# Approach #2: Min Queue 
class MinQueue:
    def __init__(self):
        deque.__init__(self)
        self.mins = deque()

    def append(self, x):
        deque.append(self, x)
        while self.mins and x < self.mins[-1]:
            self.mins.pop()
        self.mins.append(x)

    def popleft(self):
        x = deque.popleft(self)
        if self.mins[0] == x:
            self.mins.popleft()
        return x

    def min(self):
        return self.mins[0]

class Solution2:
    def kEmptySlots(self, flowers, k):
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day

        window = MinQueue()
        ans = len(days)

        for i, day in enumerate(days):
            window.append(day)
            if k <= i < len(days) - 1:
                window.popleft()
                if k == 0 or days[i-k] < window.min() > days[i+1]:
                    ans = min(ans, max(days[i-k], days[i+1]))

        return ans if ans < len(days) else -1

# Approach #3: Sliding Window
class Solution3:
    def kEmptySlots(self, flowers, k):
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day

        ans = float('inf')
        left, right = 0, k+1
        while right < len(days):
            for i in xrange(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i+k+1
                    break
            else:
                ans = min(ans, max(days[left], days[right]))
                left, right = right, right+k+1

        return ans if ans < float('inf') else -1
