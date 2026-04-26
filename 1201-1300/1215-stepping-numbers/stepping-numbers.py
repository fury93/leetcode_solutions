class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        ans = []
        if low == 0:
            ans.append(0)
        q = deque(range(1, 10))
        while q:
            v = q.popleft()
            if v > high:
                break
            if v >= low:
                ans.append(v)
            x = v % 10
            if x:
                q.append(v * 10 + x - 1)
            if x < 9:
                q.append(v * 10 + x + 1)
        return ans
        
class Solution2:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        q1, q2 = set(), collections.deque(range(10))
        while q2:
            n = q2.popleft()
            if low <= n <= high:
                q1.add(n)
            if n < high:
                d = n % 10
                if d == 0:
                    q2.append(n * 10 + 1)
                elif d == 9:
                    q2.append(n * 10 + 8)
                else:
                    q2.append(n * 10 + d + 1)
                    q2.append(n * 10 + d - 1)
        return sorted(q1)