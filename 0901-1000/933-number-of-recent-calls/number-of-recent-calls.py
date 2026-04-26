class RecentCounter:

    def __init__(self):
        self.data = deque()
        self.k = 3000
        self.calls = 0

    def ping(self, t: int) -> int:
        self.calls += 1
        if not self.data or self.data[-1][0] < t:
            self.data.append([t, 1])
        else:
            self.data[-1][0] += 1
        
        while self.data[0][0] < t - self.k:
            self.calls -= self.data.popleft()[1]
        
        return self.calls


class RecentCounter2:

    def __init__(self):
        self.data = deque()
        self.k = 3000

    def ping(self, t: int) -> int:
        self.data.append(t)
        
        return len(self.data) - bisect_left(self.data, t - self.k)

class RecentCounter3:

    def __init__(self):
        self.data = deque()
        self.k = 3000

    def ping(self, t: int) -> int:
        self.data.append(t)

        while self.data[0] < t - self.k:
            self.data.popleft()
        
        return len(self.data)

class RecentCounter4:

    def __init__(self):
        self.k = 3001
        self.data = [[0, 0]] * (self.k)

    def ping(self, t: int) -> int:
        key = t % self.k
        if self.data[key][0] != t:
            self.data[key] = [t, 1]
        else:
            self.data[key][1] += 1
        minTime = t - self.k
        
        return sum(val for time, val in self.data if time > minTime)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)